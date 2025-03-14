
# WebSockets Mejorada con FastAPI y WebSockets

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio

app = FastAPI()

html = 