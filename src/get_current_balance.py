import logging
def get_current_balance(client):
    print("FETCHING CURRENT FUTURES BALANCE...")
    try:
        balance_info = client.futures_account_balance()
        usdt_balance = next(
            (item for item in balance_info if item['asset'] == 'USDT'), None
        )
        if usdt_balance:
            print(f"CURRENT USDT BALANCE: {usdt_balance['balance']}")
            logging.info(f"Fetched USDT balance: {usdt_balance['balance']}")
            return float(usdt_balance['balance'])
        else:
            raise Exception("USDT balance not found in futures account")
    except Exception as e:
        logging.error(f"Failed to get futures balance: {e}")
        print("FUTURES BALANCE ERROR:", e)
        return None