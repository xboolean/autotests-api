import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        msg = "Привет, сервер!"
        print(f"Отправка: {msg}")
        await websocket.send(msg)
        for _ in range(5):
            message = await websocket.recv()
            print(f"Получение сообщение от сервера: {message}")

asyncio.run(client())