
import logging
import requests
from alpaca.helpers.trading_enums import OrderSide, OrderType, OrderTime
import json
from date_util import subtract_time_from_todays_date
#Alpaca Account Object Details: https://alpaca.markets/docs/api-references/trading-api/account/

class AccountAPIActions:

    def __init__(self, server_endpoint, server_key, server_secret, data_endpoint) -> None:
        self.end = f"{server_endpoint}/V2"
        self.key = server_key
        self.secret = server_secret
        
        self.headers = {
            "APCA-API-KEY-ID": f"{self.key}",
            "APCA-API-SECRET-KEY": f"{self.secret}"
        }

        self.data_end = f"{data_endpoint}/v2"

    def submitRequest(self, action="GET", urlEnd="", data=[], params=[], market_data=False):

        logging.debug(f"URL sent: {self.end if not market_data else self.data_end}/{urlEnd}")
        if action == "GET":
            response = requests.get(f"{self.end if not market_data else self.data_end}/{urlEnd}", headers=self.headers, data=data, params=params)
        elif action == "DELETE":
            response = requests.delete(f"{self.end if not market_data else self.data_end}/{urlEnd}", headers=self.headers, data=data, params=params)
        elif action == "POST":
           response = requests.post(f"{self.end if not market_data else self.data_end}/{urlEnd}", headers=self.headers, data=data, params=params)
         
       
        if response.status_code == 200:
            return response.json()
        else:
            return None
        

    #Account Actions
    def getAccountDetails(self):
        
        logging.info(f"{self.end}/account")
        response = self.submitRequest(urlEnd="account")

        if response is None:
            return None
        
        return response

    def getAllAssets(self):
        r = self.submitRequest(urlEnd="assests")
        return self.decodeAssetResponse(r)

    def getAsset(self, ticker=""):
        r = self.submitRequest(urlEnd=f"assets/{ticker}")
        return r

    #Order Actions
    def getOrders(self):

        response = self.submitRequest(urlEnd="orders")

        return response

    def getOrder(self, order_id):
        
        response = self.submitRequest(urlEnd=f"orders/{order_id}")
        
        if response.status_code == 200:
            return response.json()
        else: 
            return None

    def makeOrder(self, stock_symbol, order_amount, order_side=OrderSide.BUY, purchase_type=OrderType.MARKET, limit_price=None, order_time=OrderTime.DAY):
        #Additional Parameters can be added
        #Only adding support for market and limit purchase ATM

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
        response = self.submitRequest(urlEnd="orders",action="POST" ,data=body)

        return response
    
    #Position Actions
    
    def closePosition(self, ticker="", qty=0, percentage=0):
        body = {
            "qty" : qty,
            "percentage" : percentage
        }

        return self.submitRequest(urlEnd=f"positions/{ticker}", action="DELETE", data=body)

    def closeAllPositions(self):
        return self.submitRequest(urlEnd=f"positions", action="DELETE", data={"cancel_orders": True})
    
    def getPositions(self):
        return self.submitRequest(urlEnd="positions")

    #Historical Actions
    def getTickerSnapShot(self, symbol):

        response = self.submitRequest(urlEnd=f"stocks/{symbol}/snapshot", market_data=True)
        return response

    def getMultipleTickerSnapshots(self, symbols):

        #Change multiple snapshot response to a list of single snapshots rather than a keyword snapshot
        def clean_snapshot_response(response):
            cleaned_response = []

            
            for symbol in response:
                t = {}
                
                t["symbol"] = symbol
                t["latestTrade"] = response[symbol]["latestTrade"]
                t["latestQuote"] = response[symbol]["latestQuote"]
                t["minuteBar"] = response[symbol]["minuteBar"]
                t["dailyBar"] = response[symbol]["dailyBar"]
                t["prevDailyBar"] = response[symbol]["prevDailyBar"]

                cleaned_response.append(t)

            return cleaned_response

        symbolString = ""
        for symbol in symbols:
            symbolString += f",{symbol}"

        url = f"stocks/snapshots?symbols={symbolString[1:]}"
        response = self.submitRequest(urlEnd=url, market_data=True)

        if response is not None:
            response = clean_snapshot_response(response)

        return response
        
    def getBarFromASpecfiedDateRange(self, symbol, years=0, months=0, days=0, hours=0, minutes=0, interval = "1Day"):
        """
        Collects the historical bar information from a given stock with n_days set to 0 equaling today.
        Interval can incorpate Year, Month, Week, Day, Hour, Min up to a year and a day intervals
        """
        data = {"timeframe": f"{interval}", "start": f"{subtract_time_from_todays_date()}"}    
        response = self.submitRequest(urlEnd= "stocks/{symbol}/bars", params=data, market_data=True)    
        
        return response