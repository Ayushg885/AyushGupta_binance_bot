import logging

def place_limit_order(client, validate_inputs, symbol, side, quantity, price):
    try:
        validate_inputs(symbol, quantity, price)

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"Limit order placed: {order}")

        return order

    except Exception as e:
        logging.error(f"Limit order failed: {e}")
        print("LIMIT ORDER ERROR:", e)
        return None