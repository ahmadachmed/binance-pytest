import logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient
from binance.spot import Spot as SpotClient
import yaml

class WebSocketClient:
    def __init__(self, config_path="config/test_config.yaml"):
        self.config = self.load_config(config_path)
        testnet_status = self.config["testnet"]
        if testnet_status:
            self.websocket_base_url = self.config["testnet_websocket_base_url"]
            self.spot_base_url = self.config["testnet_base_url"]
        else:
            self.websocket_base_url = self.config["websocket_base_url"]
            self.spot_base_url = self.config["mainnet_base_url"]
        self.ws_client = SpotWebsocketStreamClient(stream_url=self.websocket_base_url, on_message=self.message_handler)
        self.spot_client = SpotClient(
            api_key=self.config["api_key"], 
            api_secret=self.config["api_secret"], 
            base_url=self.spot_base_url
        )
        self.callbacks = {}

    
    def load_config(self, config_path):
        """Load konfigurasi dari YAML file."""
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    
    def message_handler(message):
        logging.info(message)
        
    def subscribe_order_book(self, symbol, callback):
        """Subscribe to the Order Book stream."""
        self.ws_client.book_ticker(symbol=symbol, id=1, callback=callback)

    def subscribe_trade(self, symbol, callback):
        """Subscribe to the Trade stream."""
        self.ws_client.trade(symbol=symbol, id=2, callback=callback)

    def subscribe_user_data(self, callback):
        """Subscribe to the User Data stream."""
        listen_key = self.spot_client.new_listen_key()['listenKey']
        self.ws_client.user_data(listen_key=listen_key, id=3, callback=callback)
    
    def client_stop(self):
        self.ws_client.stop()