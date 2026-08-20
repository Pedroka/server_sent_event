import redis.asyncio as aioredis

class RedisConnection:
    _instance = None

    def __init__(self):
        if not hasattr(self, "initialised"):
            self.connection = aioredis.Redis(host='localhost', port=6379, decode_responses=True)
            self.initialised = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        

        return cls._instance