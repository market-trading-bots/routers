from abc import ABC, abstractmethod
from typing import Optional

from .orders import Order


class BaseExchangeRouter(ABC):
    @abstractmethod
    def send_order(self, order: Order):
        pass

    @abstractmethod
    def cancel_order(self, symbol: str, order_id: Optional[int]):
        pass

    @abstractmethod
    def get_order_status(self, symbol: str, order_id: Optional[int]):
        pass

    @abstractmethod
    def get_balance(self):
        pass
