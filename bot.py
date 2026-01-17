from time import time
from binance import Client
import logging
import os
from dotenv import load_dotenv
from src.advanced.grid import place_grid_orders
from src.advanced.twap import place_twap_orders
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from cli_str import banner, menu, clear_screen
from src.advanced.stop_limit_order import place_stop_limit_order
from src.get_current_balance import get_current_balance
load_dotenv()

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = os.getenv("binance_url")
        logging.info(f"Connected to Binance | Testnet={testnet}")
    
    def validate_inputs(self,symbol, quantity, price=None):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if price is not None and price <= 0:
            raise ValueError("Price must be greater than zero")
        logging.info(f"Inputs validated for {symbol} | Quantity={quantity} | Price={price}")

    def market_order(self, symbol, side, quantity):
        return place_market_order(
            self.client,
            self.validate_inputs,
            symbol,
            side,
            quantity
        )
    def limit_order(self, symbol, side, quantity, price):
        return place_limit_order(
            self.client,
            self.validate_inputs,
            symbol,
            side,
            quantity,
            price
        )
    def stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        return place_stop_limit_order(
            self.client,
            self.validate_inputs,
            symbol,
            side,
            quantity,
            stop_price,
            limit_price
        )
    def grid_strategy(self, symbol, lower_price, upper_price, grids, quantity):
        return place_grid_orders(
            self.client,
            self.validate_inputs,
            symbol,
            lower_price,
            upper_price,
            grids,
            quantity
        )
    def twap_strategy(self, symbol, side, total_quantity, slices, interval_sec):
        return place_twap_orders(
            self.client,
            self.validate_inputs,
            symbol,
            side,
            total_quantity,
            slices,
            interval_sec
        )
    def get_balance(self):
        return get_current_balance(self.client)


if __name__ == "__main__":
    API_KEY = os.getenv("binance_api_key")
    API_SECRET = os.getenv("binance_api_secret")
    banner()
    bot = BasicBot(API_KEY, API_SECRET, testnet=True)
    while True:
        try:
            choice = menu()
            if choice == "1":
                bot.get_balance()

            elif choice == "2":
                print("Enter the Quantity for Market Order")
                quantity = float(input("Quantity: "))
                bot.market_order("BTCUSDT", "BUY", quantity)


            elif choice == "3":
                print("Enter the Quantity to Limit Order")
                quantity = float(input("Quantity: "))
                print("Placing Limit Order to SELL Price")
                price = float(input("Enter Limit Price: "))
                bot.limit_order("BTCUSDT", "SELL", quantity, price)

            elif choice == "4":
                print("Enter the Quantity for Stop-Limit Order")
                quantity = float(input("Quantity: "))
                print("Placing Stop-Limit Order to BUY")
                stop_price = float(input("Enter Stop Price: "))
                limit_price = float(input("Enter Limit Price: "))
                bot.stop_limit_order("BTCUSDT", "BUY", quantity, stop_price, limit_price)
            
            elif choice == "5":
                print("Enter details for Grid Strategy")
                lower_price = float(input("Lower Price: "))
                upper_price = float(input("Upper Price: "))
                grids = int(input("Number of Grids: "))
                quantity = float(input("Quantity per Order: "))
                bot.grid_strategy("BTCUSDT", lower_price, upper_price, grids, quantity)
            
            elif choice == "6":
                print("Enter details for TWAP Strategy")
                side = input("Side (BUY/SELL): ").upper()
                total_quantity = float(input("Total Quantity: "))
                slices = int(input("Number of Slices: "))
                interval_sec = int(input("Interval between Slices (seconds): "))
                bot.twap_strategy("BTCUSDT", side, total_quantity, slices, interval_sec)
            
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            logging.error(f"Validation Error: {e}")