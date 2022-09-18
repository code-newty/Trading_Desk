from cmath import log
from config import SANDBOX_API_ENDPOINT, SANDBOX_API_KEY, SANDBOX_API_SECRET, DEV_API_ENDPOINT, DEV_API_KEY, DEV_API_SECRET, DATA_API_ENDPOINT
from alpaca.alpaca_api_networking import AccountAPIActions
import logging
from alpaca.helpers.trading_enums import OrderSide, OrderType, OrderTime
from alpaca.helpers.alpaca_object_tests import test_account, test_order, test_historical_bar, test_asset


end, key, secret = SANDBOX_API_ENDPOINT, SANDBOX_API_KEY, SANDBOX_API_SECRET
dev_end, dev_key, dev_secret = DEV_API_ENDPOINT, DEV_API_KEY, DEV_API_SECRET
data_end = DATA_API_ENDPOINT

def run_unittests():
    test_account()
    test_order()
    test_historical_bar()
    test_asset()
    print("Everything worked")

def main():

    logging.basicConfig(filename="logs/trading_desk.log", level=logging.DEBUG, format="%(asctime)s %(message)s",datefmt="%m/%d/%Y %I:%M:%S %p")
    run_unittests()
   
    account = AccountAPIActions(end, key, secret,data_end)
    r = account.getAsset("SPY")
    logging.info(f"Asset: {r}")
    

    


if __name__ == "__main__":
    main()
    



