from binance.spot import Spot
from binance.um_futures import UMFutures

from .base import BaseExchangeRouter
from .configs import BinanceConfig, BinanceFuturesConfig
from .orders import Order


class BinanceFuturesRouter(BaseExchangeRouter):
    def __init__(self, config: BinanceFuturesConfig):
        self.client = UMFutures(**config.to_dict())

    def send_order(self, order: Order):
        return self.client.new_order(**order.to_dict())

    def cancel_order(self, order: Order):
        return self.client.cancel_order(**order.to_dict())

    def get_order_status(self, order: Order):
        return self.client.get_all_orders(**order.to_dict())


class BinanceRouter(BaseExchangeRouter):
    def __init__(self, config: BinanceConfig):
        self.client = Spot(**config.to_dict())

    @property
    def account(self, **kwargs):
        return self.client.account(**kwargs)

    def send_order(self, order: Order):
        return self.client.new_order(**order.to_dict())

    def cancel_order(self, order: Order):
        return self.client.cancel_order(**order.to_dict())

    def get_order_status(self, order: Order):
        return self.client.get_all_orders(**order.to_dict())
