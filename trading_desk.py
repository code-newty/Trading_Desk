from config import SANDBOX_API_ENDPOINT, SANDBOX_API_KEY, SANDBOX_API_SECRET, DEV_API_ENDPOINT, DEV_API_KEY, DEV_API_SECRET, DATA_API_ENDPOINT
from alpaca_api_networking import AccountAPIActions
import logging
from trading_enums import OrderSide, OrderType, OrderTime



end, key, secret = SANDBOX_API_ENDPOINT, SANDBOX_API_KEY, SANDBOX_API_SECRET
dev_end, dev_key, dev_secret = DEV_API_ENDPOINT, DEV_API_KEY, DEV_API_SECRET
data_end = DATA_API_ENDPOINT

def main():
    logging.basicConfig(filename="trading_desk.log", level=logging.DEBUG, format="%(asctime)s %(message)s",datefmt="%m/%d/%Y %I:%M:%S %p")
    account = AccountAPIActions(end, key, secret, data_end)

if __name__ == "__main__":
    main()
    




