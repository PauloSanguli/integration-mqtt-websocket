from src.socket.client_service import SocketClient
import asyncio

if __name__=="__main__":
    SocketClient.emit_message("connected", "ws://localhost:8070/ws")