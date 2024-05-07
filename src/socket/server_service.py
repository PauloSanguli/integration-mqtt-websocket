from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio

import json

from .handler_file import get_account


app = FastAPI()
# Configure o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            if data == 'connected':
                print("connected") 
                while True:
                    await asyncio.sleep(1)
                    account_datas = get_account()
                    if len(account_datas) > 0:
                        print(account_datas)
                        await send_message_to_client(websocket, json.dumps({
                            "ref_account": account_datas[1],
                            "pin": account_datas[0]}))
    except Exception as error:
        print(error)
        print("Connection closed...")


async def send_message_to_client(websocket: WebSocket, message: str):
    """Função para emitir uma mensagem para o cliente WebSocket"""
    await websocket.send_text(message)
