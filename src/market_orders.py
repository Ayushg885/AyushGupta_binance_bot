import logging

from cli_str import banner

def place_market_order(client, validate_inputs, symbol, side, quantity):
    try:
        validate_inputs(symbol, quantity)

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        if not order:
            raise Exception("Empty response from Binance API")

        logging.info(f"Market order placed: {order}")
        print("MARKET ORDER PLACED SUCCESSFULLY")

        return order
    
    except Exception as e:
        logging.error(f"Market order failed: {e}")
        print("MARKET ORDER ERROR:", e)
        return None