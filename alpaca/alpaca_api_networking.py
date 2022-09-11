from cgitb import reset
import logging
import requests
from trading_enums import OrderSide, OrderType, OrderTime
import json
from date_util import subtract_time_from_todays_date
#Alpaca Account Object Details: https://alpaca.markets/docs/api-references/trading-api/account/

class AccountAPIActions:

    def __init__(self, server_endpoint, server_key, server_secret, data_endpoint) -> None:
        self.end = f"https://{server_endpoint}/V2"
        self.key = server_key
        self.secret = server_secret
        
        self.headers = {
            "APCA-API-KEY-ID": f"{self.key}",
            "APCA-API-SECRET-KEY": f"{self.secret}"
        }

        self.data_end = f"https://{data_endpoint}/v2"

    def getAccountDetails(self):
        
        logging.info(f"{self.end}/account")
        response = requests.get(f"{self.end}/account", headers=self.headers)
        
        if response.status_code == 200:
            
            jsonResponse = response.json()  
            return jsonResponse
        
        return None

    def getAccountPositions(self):
        pass

    def createPosition(self, stock_symbol, order_amount, order_side=OrderSide.BUY, purchase_type=OrderType.MARKET, limit_price=None, order_time=OrderTime.DAY):
        #Additional Parameters can be added
        #Only adding support for market and limit purchase ATM


        logging.debug(self.headers)
        logging.debug(f"{self.end}/orders")
        #Prerequiste body parameters that apply to any order type
        body = {
                    "symbol": stock_symbol,
                    "qty": str(order_amount),
                    "side": order_side.value,
                    "type": purchase_type.value,
                    "time_in_force": order_time.value
                }

        if purchase_type is OrderType.LIMIT: 
            if limit_price is None:
                logging.warning("Limit purchase not provided")
                return None
            elif limit_price <= 0:
                logging.info("Price set for purchase is 0, too low for any purchase to be made")
                return None
            else:
                body["limit_price"] = limit_price

        #Create and send request
        body = json.dumps(body)
        logging.debug(body)
        response = requests.post(f"{self.end}/orders", headers=self.headers,data=body)

        if response.status_code == 200:
            return response.json()
        else:
            logging.debug(response.text)
            return None
    
    def getOrders(self):

        response = requests.get(f"{self.end}/orders", headers=self.headers)

        if response.status_code == 200:
            return response.json()
        
        return None

    def getOrder(self, order_id):
        
        response = requests.get(f"{self.end}/orders/{order_id}", headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else: 
            return None

    def getTickerSnapShot(self, symbol):

        response = requests.get(f"https://data.alpaca.markets/v2/stocks/{symbol}/snapshot", headers=self.headers)

        if response.status_code == 200:
            return response.json()
        
        else:
             return None

    def getMultipleTickerSnapshots(self, symbols):

        symbolString = ""
        for symbol in symbols:
            symbolString += f",{symbol}"

        url = f"{self.data_end}/stocks/snapshots?symbols={symbolString[1:]}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        
        else:
            return None
        
    def getBarFromASpecfiedDateRange(self, symbol, years=0, months=0, days=0, hours=0, minutes=0, interval = "1Day"):
        """
        Collects the historical bar information from a given stock with n_days set to 0 equaling today.
        Interval can incorpate Year, Month, Week, Day, Hour, Min up to a year and a day intervals
        """
        data = {"timeframe": f"{interval}", "start": f"{subtract_time_from_todays_date()}"}        
        response = requests.get(f"{self.data_end}/stocks/{symbol}/bars", headers=self.headers,params=data)

        if response.status_code == 200:
            logging.info(response.json())