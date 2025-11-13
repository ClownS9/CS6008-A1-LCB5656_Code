import asyncio
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(".__main__:app", host="127.0.0.1", port=9000, reload=True)