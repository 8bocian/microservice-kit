from __future__ import annotations

from aio_pika.abc import AbstractIncomingMessage, AbstractRobustConnection, AbstractRobustChannel
from aio_pika import connect_robust, Message
from typing import Dict, Callable, Awaitable


class RabbitMQ(BaseLifecycleComponent):
    def __init__(self, publisher: BaseRabbiMQPublisher, consumer: BaseRabbitMQConsumer):
        self.publisher = publisher
        self.consumer = consumer

    async def start(self):
        self.pub_connection = await connect_robust(self._rabbitmq_url)
        self.pub_channel = self.pub_connection.channel()

        self.con_connection = await connect_robust(self._rabbitmq_url)
        for queue_name, handler in self.con_handlers.items():
            channel = self.con_connection.channel()

            self.con_channels[queue_name] = channel

    async def stop(self):
        if self.pub_channel:
            await self.pub_channel.close()
        if self.pub_connection:
            await self.pub_connection.close()

        for channel in self.con_channels.values():
            if channel:
                await channel.close()

        if self.con_connection:
            await self.con_connection.close()