from .lifecycle_component import BaseLifecycleComponent
from abc import ABC

class BaseEventBus(BaseLifecycleComponent, ABC):
    publisher: BaseEventPublisher
    consumer: BaseEventConsumer