import pytest


@pytest.mark.parametrize("symbol, side, quantity, price", [
    ("BTCUSDT", "BUY", 0.001, "30000"),
    ("BTCUSDT", "BUY", 0.002, "31000"),
    ("BTCUSDT", "SELL", 0.001, "32000"),
])
def test_place_limit_order(api_client, symbol, side, quantity, price):
    response = api_client.place_limit_order(symbol=symbol, side=side, quantity=quantity, price=price)
    assert "orderId" in response, 'There is no orderId from the response'
    assert response["symbol"] == symbol, f'There is no symbol: {symbol} from the response'
    assert response["side"] == side, f'There is no side: {side} from the response'