from abc import ABC, abstractmethod

from microservice_kit.interfaces.lifecycle_component import BaseLifecycleComponent


class BaseEventPublisher(BaseLifecycleComponent, ABC):
    @abstractmethod
    async def publish(self, topic: str, event: dict) -> None:...