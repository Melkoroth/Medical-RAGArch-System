
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from mangum import Mangum

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"Mensaje: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Compatibilidad con AWS Lambda
handler = Mangum(app, lifespan="auto")
