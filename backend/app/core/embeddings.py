from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import uuid

# Persistent Chroma client
chroma_client = chromadb.PersistentClient(path="/backend/chromaVecDB")

collection = chroma_client.get_or_create_collection("transcript_chunks")

# Embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Standard chunk splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

def add_transcript_to_vector_db(conversation_id: str, text: str):
    chunks = splitter.split_text(text)
    embeddings = embedding_model.encode(chunks, convert_to_numpy=True)
    # Store in Chroma
    for chunk_text, emb in zip(chunks, embeddings):
        collection.add(
            documents=[chunk_text],
            metadatas=[{"conversation_id": conversation_id}],
            embeddings=[emb],
            ids = [str(uuid.uuid4())]
        )
    print(collection.count())

def query_vector_db(query: str, top_k: int = 5):
    query_embedding = embedding_model.encode([query], convert_to_numpy=True)
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
        include=["documents", "metadatas"]
    )
    
    return results["documents"][0]
    
def delete_conversation(conversation_id: str):
    # delete all chunks with this conversation_id
    collection.delete(where={"conversation_id": conversation_id})