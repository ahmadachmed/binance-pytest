import pytest
from src.websocket_client import WebSocketClient

@pytest.fixture(scope="module")
def ws_client():
    client = WebSocketClient()
    yield client
    client.client_stop()