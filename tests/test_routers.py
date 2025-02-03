import os

import pytest

import routers
from routers.base import BaseExchangeRouter
from routers.orders import Order

EXCHANGES = ("BinanceFutures",)


@pytest.fixture
def setup_router(exchange):
    """Fixture to initialize router with testnet settings."""
    os.environ[f"{exchange.upper()}_TESTNET"] = "True"
    config = getattr(routers.configs, f"{exchange}Config").from_env()
    router = getattr(routers, f"{exchange}Router")(config)
    assert isinstance(
        router, BaseExchangeRouter
    ), f"Router {exchange} is not initialized properly."
    return router


@pytest.mark.parametrize("exchange", EXCHANGES)
def test_router(setup_router, exchange):
    router = setup_router

    # Get initial balance
    initial_balance = router.get_balance()
    assert initial_balance is not None, f"Failed to fetch balance for {exchange}."

    # Create a test order
    test_order = Order(
        symbol="BTCUSDT",
        side="BUY",
        type="LIMIT",
        quantity=1,
        price=1_000,
        timeInForce="GTC",
    )

    # Place order
    order_response = router.send_order(test_order)
    order_id = order_response.get("orderId")
    assert order_id, f"Order placement failed on {exchange}, response: {order_response}"

    # Verify order is placed
    placed_orders = router.get_order_status(symbol="BTCUSDT")
    assert any(
        o["orderId"] == order_id for o in placed_orders
    ), f"Order {order_id} not found in {exchange} orders."

    # Cancel order
    router.cancel_order(test_order.symbol, order_id)

    # Ensure order is canceled
    remaining_orders = router.get_order_status(symbol="BTCUSDT")
    assert not any(
        o["orderId"] == order_id for o in remaining_orders
    ), f"Order {order_id} not canceled on {exchange}."

    # Verify balance remains the same
    final_balance = router.get_balance()
    assert (
        final_balance == initial_balance
    ), f"Balance mismatch on {exchange}: {initial_balance} -> {final_balance}"
