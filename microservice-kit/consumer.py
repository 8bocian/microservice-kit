from typing import Callable
import aio_pika

class RabbitMQConsumer:
    def __init__(self, url: str):
        self.url = url
        self.connection: aio_pika.RobustConnection | None = None
        self._channels: dict[str, aio_pika.abc.AbstractRobustChannel] = {}
        self._handlers: dict[str, Callable] = {}

    def add_handler(self, queue_name: str, handler: Callable):
        """Add handler"""
        self._handlers[queue_name] = handler

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.url)
        for queue_name, handler in self._handlers.items():
            channel = await self.connection.channel()
            self._channels[queue_name] = channel
            queue = await channel.declare_queue(queue_name, durable=True)
            await queue.consume(handler)

    async def close(self):
        for channel in self._channels.values():
            await channel.close()
        if self.connection:
            await self.connection.close()