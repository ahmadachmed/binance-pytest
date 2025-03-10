from binance.spot import Spot
import yaml

class APIClient:
    def __init__(self, config_path="config/test_config.yaml"):
        self.config = self.load_config(config_path)
        testnet_status = self.config["testnet"]
        if testnet_status:
            self.base_url = self.config["testnet_base_url"]
        else:
            self.base_url = self.config["mainnet_base_url"]
        self.client = Spot(
            api_key=self.config["api_key"], 
            api_secret=self.config["api_secret"], 
            base_url=self.base_url
        )

    def load_config(self, config_path):
        """Load konfigurasi dari YAML file."""
        with open(config_path, "r") as f:
            return yaml.safe_load(f)

    def get_order_book(self, symbol="BTCUSDT", limit=5):
        """Fetch order book."""
        return self.client.depth(symbol=symbol, limit=limit)

    def place_limit_order(self, symbol, side, quantity, price):
        """Place a limit order."""
        return self.client.new_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=str(price),
        )

    def get_open_orders(self, symbol="BTCUSDT"):
        """Fetch open orders."""
        return self.client.get_open_orders(symbol=symbol)

    def get_trade_history(self, symbol="BTCUSDT"):
        """Fetch trade history."""
        return self.client.my_trades(symbol=symbol)

    def get_account_balance(self):
        """Fetch account balance."""
        return self.client.account()