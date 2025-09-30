from .event_consumer import BaseEventConsumer
from .event_publisher import BaseEventPublisher
from abc import ABC, abstractmethod


class BaseEventBus(BaseEventPublisher, BaseEventConsumer, ABC):
    pass