from dataclasses import asdict, dataclass


@dataclass
class Order:
    symbol: str
    side: str
    type: str
    quantity: float
    price: float
    id: str = None

    def to_dict(self) -> dict:
        return asdict(self)
