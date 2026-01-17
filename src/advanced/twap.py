import time
import logging

def place_twap_orders(
    client,
    validate_inputs,
    symbol,
    side,
    total_quantity,
    slices,
    interval_sec
):
    try:
        if slices <= 0:
            raise ValueError("Slices must be greater than zero")

        if interval_sec <= 0:
            raise ValueError("Interval must be greater than zero")
        qty_per_order = round(total_quantity / slices, 6)

        validate_inputs(symbol, qty_per_order)

        orders = []

        for i in range(slices):
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=qty_per_order
            )

            orders.append(order)

            logging.info(
                f"TWAP order {i+1}/{slices} placed: {order}"
            )

            print(
                f"TWAP {i+1}/{slices} | Qty={qty_per_order} executed"
            )

            # Wait before next slice
            if i < slices - 1:
                time.sleep(interval_sec)

        print("TWAP STRATEGY COMPLETED")
        return orders

    except Exception as e:
        logging.error(f"TWAP strategy failed: {e}")
        print("TWAP ERROR:", e)
        return None
