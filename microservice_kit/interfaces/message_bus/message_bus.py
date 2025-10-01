from .message_consumer import BaseMessageConsumer
from .message_publisher import BaseMessagePublisher
from abc import ABC, abstractmethod


class BaseMessageBus(BaseMessagePublisher, BaseMessageConsumer, ABC):
    pass