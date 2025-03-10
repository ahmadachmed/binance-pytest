import pytest

def test_get_open_orders(api_client):
    order = api_client.place_limit_order(symbol="BTCUSDT", side="BUY", quantity=0.001, price="30000")
    order_id = order["orderId"]
    response = api_client.get_open_orders("BTCUSDT")
    assert any(order["orderId"] == order_id for order in response), f"Order ID: {order_id} not found from the response"