import uvicorn

from app.main import app

PORT = 8000

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=PORT)
