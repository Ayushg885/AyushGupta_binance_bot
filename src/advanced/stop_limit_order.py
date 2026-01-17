import logging

def place_stop_limit_order(
    client,
    validate_inputs,
    symbol,
    side,
    quantity,
    stop_price,
    limit_price
):
    try:
        validate_inputs(symbol, quantity, limit_price)

        if stop_price <= 0:
            raise ValueError("Stop price must be greater than zero")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            stopPrice=stop_price,
            price=limit_price,
            timeInForce="GTC"
        )

        logging.info(f"Stop-Limit order placed: {order}")
        print("STOP-LIMIT ORDER PLACED:", order)

        return order

    except Exception as e:
        logging.error(f"Stop-Limit order failed: {e}")
        print("STOP-LIMIT ERROR:", e)
        return None
