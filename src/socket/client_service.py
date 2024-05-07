import websocket


class SocketClient:
    @staticmethod
    def emit_message(message: str, uri: str):
        """config and set message to server"""
        conn = websocket.create_connection("ws://localhost:8070/ws")
        conn.send("connected")
        data = conn.recv()
        print(data)
