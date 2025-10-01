from microservice_kit.interfaces.lifecycle_component import BaseLifecycleComponent
from microservice_kit.interfaces.message_bus.models.envelope import Envelope
from abc import ABC, abstractmethod


class BaseMessagePublisher(BaseLifecycleComponent, ABC):
    @abstractmethod
    async def publish(self, envelope: Envelope) -> None:
        """Publish envelope to be sent

        :param envelope: Envelope with Routing informing about destination and Message it means to deliver
        :return: None
        """
        ...