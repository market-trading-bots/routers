from abc import ABC, abstractmethod
from typing import Any, Optional

from .orders import Order


class BaseExchangeRouter(ABC):
    @abstractmethod
    def send_order(self, order: Order) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_order(self, symbol: str, order_id: Optional[int]) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_order_status(self, symbol: str, order_id: Optional[int]) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_balance(self) -> dict[str, Any]:
        pass
