def test_get_order_book(api_client):
    response = api_client.get_order_book(symbol="BTCUSDT", limit=5)
    assert "bids" in response and "asks" in response, "bids and asks not found from the response"
    assert len(response["bids"]) > 0, "Bids should be greater than 0"
    assert len(response["asks"]) > 0, "Asks should be greater than 0"