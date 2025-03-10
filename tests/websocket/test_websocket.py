def test_order_book_stream(ws_client):
    def callback(message):
        assert 'e' in message  # Event type
        assert 'E' in message  # Event time
        assert 's' in message  # Symbol
        assert 'b' in message  # Bids
        assert 'a' in message  # Asks

    ws_client.subscribe_order_book(symbol="btcusdt", callback=callback)

def test_trade_stream(ws_client):
    def callback(message):
        assert 'e' in message  # Event type
        assert 'E' in message  # Event time
        assert 's' in message  # Symbol
        assert 't' in message  # Trade ID
        assert 'p' in message  # Price
        assert 'q' in message  # Quantity

    ws_client.subscribe_trade(symbol="btcusdt", callback=callback)

def test_user_data_stream(ws_client):
    def callback(message):
        assert 'e' in message  # Event type
        assert 'E' in message  # Event time
        assert 's' in message  # Symbol
        assert 'c' in message  # Client order ID
        assert 'S' in message  # Side
        assert 'o' in message  # Order type
        assert 'f' in message  # Time in force
        assert 'q' in message  # Quantity
        assert 'p' in message  # Price

    ws_client.subscribe_user_data(callback=callback)