from ast import Or
from asyncio.log import logger
import logging
from re import T
from tracemalloc import Snapshot
import unittest
import json
from alpaca.helpers.alpaca_objects import Account, Order, Snapshot, Asset
from alpaca.helpers.alpaca_test_responses import sample_test_account, sample_test_order, sample_test_historicalBar, sample_asset

def test_account():

    t = json.dumps(sample_test_account)

    
    sample_account = json.loads(t)

    test_account = Account(**sample_account)

    assert(test_account.account_number) == "PA3TTDISW3W5"

def test_order():
    test_orders = []

    t = json.dumps(sample_test_order)
    t = json.loads(t)

    for sample_order in t:
        test_orders.append(Order(**sample_order))

    assert(test_orders[1].id) == '312714de-57fe-4548-9a73-7adfbcc6f7a3'
    
def test_historical_bar(test_historical_bar=""):
    

    if test_historical_bar == "":
        test_historical_bar = sample_test_historicalBar
            
    t = json.dumps(test_historical_bar)
    t = json.loads(t)

    if type(test_historical_bar) is dict:
        logging.info(f"Bar Info: {t}")
        test_historical_bar = Snapshot(**t)
        

        assert(test_historical_bar.symbol) == "GOOG"
        assert(test_historical_bar.latestTrade.t) == "2022-09-16T19:59:59.461566836Z"
        assert(test_historical_bar.latestQuote.t) == '2022-09-16T20:00:00.000660247Z'
        assert(test_historical_bar.minuteBar.o) == 103.77

        return

    else:
        bars = []
        for historical_bar in test_historical_bar:
            bars.append(Snapshot(**historical_bar))

        assert(bars[0].symbol) == "AAPL"
        assert(bars[0].latestTrade.t) == "2022-09-16T19:59:59.901959883Z"
        assert(bars[0].latestQuote.t) == '2022-09-16T20:00:48.017824399Z'
        assert(bars[0].minuteBar.o) == 150.87

def test_asset():

    test_asset = Asset(**sample_asset)

    assert(test_asset.id) == "b28f4066-5c6d-479b-a2af-85dc1a8f16fb"