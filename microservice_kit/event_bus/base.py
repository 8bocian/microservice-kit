from abc import ABC

from microservice_kit.interfaces.lifecycle_component import BaseLifecycleComponent


class BaseRabbitMQApp(BaseLifecycleComponent, ABC):
    publisher: BaseEventPublisher
    consumer: BaseEventConsumer