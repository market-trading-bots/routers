from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class Order:
    symbol: str  # e.g. BTCUSDT
    side: str  # e.g. BUY or SELL
    type: str  # e.g.  MARKET / LIMIT / STOP / TAKE_PROFIT
    quantity: float  # e.g. 0.1
    price: Optional[float]  # price is none in case of market order
    timeInForce: Optional[str] = None  # needed for limit orders e.g. GTC / IOC / FOK
    id: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)
