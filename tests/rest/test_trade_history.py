import pytest

@pytest.mark.parametrize("symbol, quantity, price",[("BTCUSDT", 0.001, "30000")])
def test_trade_history(api_client, symbol, quantity, price):
    order = api_client.place_limit_order(symbol=symbol, side="SELL", quantity=quantity, price=price)
    order_id = order["orderId"]

    trades = api_client.get_trade_history(symbol)
    assert trades, "Trade history should not be empty"

    matched_trade = next((trade for trade in trades if trade["orderId"] == order_id), None)
    assert matched_trade, f"Order {order_id} not found in trade history"

    assert float(matched_trade["price"]) > 0, "Trade price should be valid"
    assert float(matched_trade["qty"]) == quantity, "Trade quantity should match the order"
    assert matched_trade["time"] > 0, "Trade timestamp should be valid"
