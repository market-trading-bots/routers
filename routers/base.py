from abc import ABC, abstractmethod

from .orders import Order


class BaseExchangeRouter(ABC):
    @abstractmethod
    def send_order(self, order: Order):
        pass

    @abstractmethod
    def cancel_order(self, order: Order):
        pass

    @abstractmethod
    def get_order_status(self, order: Order):
        pass
