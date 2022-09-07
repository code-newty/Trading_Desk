from enum import Enum

class OrderSide(Enum):
    BUY = "buy"
    SELL = "sell"

class OrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"
    STOP_Limit = "stop_limit"
    TRAILING_STOP = "trailing_stop"

class OrderTime(Enum):
    DAY = "day"
    GTC = "gtc" #Good Until Canceled
    OPG = "opg" #On market open
    CLS = "cls" #On market close
    IOC = "ioc" #Immediate or cancel
    FOK = "fok" #Fill or kill
