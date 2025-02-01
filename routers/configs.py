from __future__ import annotations

import os
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass


class BaseRouterConfig(ABC):
    @abstractmethod
    def from_env(cls) -> BaseRouterConfig:
        """
        Abstract method to create a configuration object from environment variables.
        Must be implemented by subclasses.
        """
        pass


@dataclass
class BinanceFuturesConfig(BaseRouterConfig):
    key: str
    secret: str
    base_url: str = "https://fapi.binance.com"

    @classmethod
    def from_env(cls) -> BinanceFuturesConfig:
        """
        Creates a BinanceFuturesConfig instance using environment variables.

        :return: A BinanceFuturesConfig instance.
        """
        api_key = os.environ.get("BINANCEFUTURES_API_KEY")
        secret_key = os.environ.get("BINANCEFUTURES_SECRET_KEY")
        base_url = (
            "https://testnet.binancefuture.com"
            if os.environ.get("BINANCEFUTURES_TESTNET", "True").lower() == "true"
            else None
        )

        if not api_key or not secret_key:
            raise ValueError(
                "Environment variables BINANCEFUTURES_API_KEY and BINANCEFUTURES_SECRET_KEY are required."
            )

        return cls(api_key, secret_key, base_url)

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass
class BinanceConfig(BaseRouterConfig):
    api_key: str
    api_secret: str
    base_url: str = "https://api.binance.com"

    @classmethod
    def from_env(cls) -> BinanceConfig:
        """
        Creates a BinanceFuturesConfig instance using environment variables.

        :return: A BinanceFuturesConfig instance.
        """
        api_key = os.environ.get("BINANCE_API_KEY")
        secret_key = os.environ.get("BINANCE_SECRET_KEY")
        base_url = (
            "https://testnet.binance.vision"
            if os.environ.get("BINANCE_TESTNET", "True").lower() == "true"
            else None
        )

        if not api_key or not secret_key:
            raise ValueError(
                "Environment variables BINANCE_API_KEY and BINANCE_SECRET_KEY are required."
            )

        return cls(api_key, secret_key, base_url)

    def to_dict(self) -> dict[str, str]:
        return asdict(self)
