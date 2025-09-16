from .publisher import RabbitMQPublisher
from .consumer import RabbitMQConsumer


class MessagingApp:
    def __init__(self, rabbit_url: str):
        self.rabbit_url = rabbit_url
        self.publisher = RabbitMQPublisher(rabbit_url)
        self.consumer = RabbitMQConsumer(rabbit_url)

    def subscribe(self, queue_name: str):
        """Handler registration decorator"""
        def decorator(func):
            self.consumer.add_handler(queue_name, func)
            return func
        return decorator

    async def start(self):
        await self.publisher.connect()
        await self.consumer.connect()

    async def stop(self):
        await self.publisher.close()
        await self.consumer.close()
