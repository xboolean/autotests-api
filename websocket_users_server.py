import asyncio

import websockets
from websockets import ServerConnection


async def async_range(start, stop):
    for i in range(start, stop):
        yield i
        await asyncio.sleep(0)


async def echo(webscocket: ServerConnection):
    async for message in webscocket:
        print(f"Получено сообщение от пользователя: {message}")
        for idx in range(1, 6):
            response = f"{idx} Сообщение пользователя: {message}"
            await webscocket.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())