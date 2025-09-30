from aio_pika import Message, connect_robust
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel
from microservice_kit.interfaces.event_bus.event_publisher import BaseEventPublisher


class RabbitMQPublisher(BaseEventPublisher):
    def __init__(self, rabbitmq_url: str):
        self._rabbitmq_url = rabbitmq_url

        self.pub_connection: AbstractRobustConnection | None = None
        self.pub_channel: AbstractRobustChannel | None = None

    async def publish(self, queue_name: str, body: str):
        if not self.pub_channel:
            raise RuntimeError("Publisher not connected")
        await self.pub_channel.default_exchange.publish(
            Message(body=body.encode()),
            routing_key=queue_name
        )

    async def build(self):
        ...

    async def start(self):
        await self.build()
        self.pub_connection = await connect_robust(self._rabbitmq_url)
        self.pub_channel = self.pub_connection.channel()

    async def stop(self):
        if self.pub_channel:
            await self.pub_channel.close()
        if self.pub_connection:
            await self.pub_connection.close()
