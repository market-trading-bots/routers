from typing import Any, Optional

from binance.spot import Spot
from binance.um_futures import UMFutures

from .base import BaseExchangeRouter
from .configs import BinanceConfig, BinanceFuturesConfig
from .orders import Order


class BinanceFuturesRouter(BaseExchangeRouter):
    exchange = "BinanceFutures"

    def __init__(self, config: BinanceFuturesConfig):
        self.client = UMFutures(**config.to_dict())

    def send_order(self, order: Order) -> dict[str, Any]:
        return self.client.new_order(**order.to_dict())

    def cancel_order(self, symbol: str, order_id: Optional[int]) -> dict[str, Any]:
        return self.client.cancel_order(symbol, orderId=order_id)

    def get_order_status(
        self, order_id: Optional[int], symbol: Optional[str]
    ) -> list[dict[str, Any]]:
        return self.client.get_orders(orderId=order_id)

    def get_balance(self) -> dict[str, Any]:
        return self.client.balance()

    def get_book_ticker(self, symbol: str) -> dict[str, str]:
        return self.client.book_ticker(symbol=symbol)


class BinanceRouter(BaseExchangeRouter):
    exchange = "Binance"

    def __init__(self, config: BinanceConfig):
        self.client = Spot(**config.to_dict())

    def send_order(self, order: Order) -> dict[str, Any]:
        return self.client.new_order(**order.to_dict())

    def cancel_order(self, symbol: str, order_id: Optional[int]) -> dict[str, Any]:
        return self.client.cancel_order(symbol, orderId=order_id)

    def get_order_status(
        self, order_id: Optional[int], symbol: Optional[str]
    ) -> list[dict[str, Any]]:
        return self.client.get_orders(symbol=symbol, orderId=order_id)

    def get_balance(self) -> dict[str, Any]:
        return self.client.account()["balances"]

    def get_book_ticker(self, symbol: str) -> dict[str, str]:
        return self.client.book_ticker(symbol=symbol)
