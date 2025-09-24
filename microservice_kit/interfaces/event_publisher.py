from microservice_kit.interfaces.lifecycle_component import BaseLifecycleComponent
from .types import Event
from abc import ABC, abstractmethod


class BaseEventPublisher(BaseLifecycleComponent, ABC):
    @abstractmethod
    async def publish(self, queue: str, event: Event) -> None:...