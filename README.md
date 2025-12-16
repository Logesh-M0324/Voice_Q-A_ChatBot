# Run the redis-memory using docker

1️⃣ Install Docker Desktop (once)

Download & install:
👉 https://www.docker.com/products/docker-desktop/

⚠️ During install:

Enable WSL 2

Restart your system if asked

Verify after install:

# docker --version

2️⃣ Run Redis container or manually run in the docker

# docker run -d -p 6379:6379 --name redis-memory redis


Check it’s running:

# docker ps

3️⃣ Test Redis , use this to run the redis our project

# docker exec -it redis-memory redis-cli ping


✅ Expected output:

PONG

4️⃣ Restart your FastAPI backend

# uvicorn app.main:app --reload


What is FFmpeg?

FFmpeg is a powerful, open-source multimedia framework used for converting, recording, streaming, editing, and playing audio and video files across almost any format.