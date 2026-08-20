from fastapi import FastAPI, Request, Response
from fastapi.responses import StreamingResponse
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from src.resources.redis_connector import RedisConnection
import json

app = FastAPI()

origins = [
    "http://localhost:52330"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Autoriza os domínios da lista
    allow_credentials=True,          # Permite o envio de cookies e dados de sessão
    allow_methods=["*"],             # Permite todos os métodos (GET, POST, PUT, etc.)
    allow_headers=["*"],             # Permite todos os cabeçalhos
)


async def redis_listen():
    client = RedisConnection()
    pubsub = client.connection.pubsub()
    await pubsub.subscribe('notification')

    while True:
        message = await pubsub.get_message(ignore_subscribe_messages=True)
        if message and message['type'] == 'message':
            yield f"event:notification\ndata:{json.dumps(message['data'])}\n\n"

        await asyncio.sleep(0.01)


@app.get('/')
def root():
    return {'Pagina principal'}


@app.get("/stream_data")
async def stream_events():
    headers = {
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
    }

    return StreamingResponse(
        redis_listen(), 
        media_type="text/event-stream",
        headers=headers
    )