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
    def get_order_status(
        self, order_id: Optional[int], symbol: Optional[str]
    ) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def get_balance(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_book_ticker(self, symbol: str) -> dict[str, str]:
        pass
