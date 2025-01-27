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
