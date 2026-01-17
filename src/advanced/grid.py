import logging

def place_grid_orders(
    client,
    validate_inputs,
    symbol,
    lower_price,
    upper_price,
    grids,
    quantity
):
    try:
        if lower_price >= upper_price:
            raise ValueError("Lower price must be less than upper price")

        if grids <= 0:
            raise ValueError("Grid count must be positive")

        validate_inputs(symbol, quantity)

        step = (upper_price - lower_price) / grids

        orders = []

        for i in range(grids):
            buy_price = round(lower_price + i * step, 2)
            sell_price = round(buy_price + step, 2)
            buy_order = client.futures_create_order(
                symbol=symbol,
                side="BUY",
                type="LIMIT",
                quantity=quantity,
                price=buy_price,
                timeInForce="GTC"
            )

            sell_order = client.futures_create_order(
                symbol=symbol,
                side="SELL",
                type="LIMIT",
                quantity=quantity,
                price=sell_price,
                timeInForce="GTC"
            )

            orders.append((buy_order, sell_order))

            logging.info(
                f"Grid order placed | BUY={buy_price}, SELL={sell_price}"
            )

        print(f"GRID STRATEGY DEPLOYED: {len(orders)} levels")
        return orders

    except Exception as e:
        logging.error(f"Grid strategy failed: {e}")
        print("GRID ERROR:", e)
        return None
