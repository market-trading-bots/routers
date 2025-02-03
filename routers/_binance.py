from typing import Optional

from binance.spot import Spot
from binance.um_futures import UMFutures

from .base import BaseExchangeRouter
from .configs import BinanceConfig, BinanceFuturesConfig
from .orders import Order


class BinanceFuturesRouter(BaseExchangeRouter):
    exchange = "BinanceFutures"

    def __init__(self, config: BinanceFuturesConfig):
        self.client = UMFutures(**config.to_dict())

    def send_order(self, order: Order):
        return self.client.new_order(**order.to_dict())

    def cancel_order(self, symbol: str, order_id: Optional[int]):
        return self.client.cancel_order(symbol, orderId=order_id)

    def get_order_status(self, symbol: str, order_id: Optional[int] = None):
        return self.client.get_orders(symbol=symbol)

    def get_balance(self):
        return self.client.balance()


class BinanceRouter(BaseExchangeRouter):
    exchange = "Binance"

    def __init__(self, config: BinanceConfig):
        self.client = Spot(**config.to_dict())

    @property
    def account(self, **kwargs):
        return self.client.account(**kwargs)

    def send_order(self, order: Order):
        return self.client.new_order(**order.to_dict())

    def cancel_order(self, symbol: str, order_id: Optional[int]):
        return self.client.cancel_order(symbol, orderId=order_id)

    def get_order_status(self, symbol: str, order_id: Optional[int]):
        return self.client.get_orders(symbol=symbol)

    def get_balance(self):
        return self.client.balance()
