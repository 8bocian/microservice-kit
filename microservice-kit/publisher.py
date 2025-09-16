import aio_pika

class RabbitMQPublisher:
    def __init__(self, url: str):
        self.url = url
        self.connection: aio_pika.RobustConnection | None = None
        self._channel: aio_pika.RobustChannel | None = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.url)
        self._channel = await self.connection.channel()

    async def publish(self, queue: str, message: str):
        await self._channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=queue,
        )

    async def close(self):
        if self.connection:
            await self.connection.close()