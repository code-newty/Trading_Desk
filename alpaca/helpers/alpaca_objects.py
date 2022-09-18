class Account:
    def __init__(
        self, 
        id, 
        account_number,
        account_blocked,
        accrued_fees, 
        buying_power,
        cash, 
        created_at, 
        currency, 
        crypto_status,
        daytrade_count,
        daytrading_buying_power,
        equity, 
        initial_margin,
        last_equity,
        last_maintenance_margin,
        long_market_value,
        maintenance_margin,
        multiplier,
        non_marginable_buying_power,
        pattern_day_trader, 
        portfolio_value,
        pending_transfer_in,
        regt_buying_power,
        short_market_value,
        shorting_enabled,
        sma,
        status,
        trade_suspended_by_user,
        trading_blocked,
        transfers_blocked
        ):

        self.id=id
        self.account_number=account_number
        self.account_blocked=account_blocked
        self.accrued_fees=accrued_fees
        self.buying_power=buying_power
        self.cash=cash
        self.created_at=created_at
        self.currency=currency
        self.crypto_status=crypto_status
        self.daytrade_count=daytrade_count
        self.daytrading_buying_power=daytrading_buying_power
        self.equity=equity
        self.initial_margin=initial_margin
        self.last_equity=last_equity
        self.last_maintenance_margin=last_maintenance_margin
        self.long_market_value=long_market_value
        self.maintenance_margin=maintenance_margin
        self.multiplier=multiplier
        self.non_marginable_buying_power=non_marginable_buying_power
        self.pattern_day_trader=pattern_day_trader
        self.portfolio_value=portfolio_value
        self.pending_transfer_in=pending_transfer_in
        self.regt_buying_power=regt_buying_power
        self.short_market_value=short_market_value
        self.shorting_enabled=shorting_enabled,
        self.sma=sma
        self.status=status
        self.trade_suspended_by_user=trade_suspended_by_user
        self.trading_blocked=trading_blocked
        self.transfers_blocked=transfers_blocked

class Order:
    def __init__(self, 
        id,
        client_order_id,
        created_at,
        updated_at,
        submitted_at,
        filled_at,
        expired_at,
        canceled_at,
        failed_at,
        replaced_at,
        replaced_by,
        replaces,
        asset_id,
        symbol,
        asset_class,
        notional,
        qty,
        filled_qty,
        filled_avg_price,
        order_class,
        order_type,
        type,
        side,
        subtag,
        time_in_force,
        limit_price,
        stop_price,
        status,
        source,
        extended_hours,
        legs,
        trail_percent,
        trail_price,
        hwm):

        
        self.id=id
        self.client_order_id=client_order_id
        self.created_at=created_at
        self.updated_at=updated_at
        self.submitted_at=submitted_at
        self.filled_at=filled_at
        self.expired_at=expired_at
        self.canceled_at=canceled_at
        self.failed_at=failed_at
        self.replaced_at=replaced_at
        self.replaced_by=replaced_by
        self.replaces=replaces
        self.asset_id=asset_id
        self.symbol=symbol
        self.asset_class=asset_class
        self.notional=notional
        self.qty=qty
        self.filled_qty=filled_qty
        self.filled_avg_price=filled_avg_price
        self.order_class=order_class
        self.order_type=order_type
        self.type=type
        self.side=side
        self.time_in_force=time_in_force
        self.limit_price=limit_price
        self.stop_price=stop_price
        self.status=status
        self.subtag=subtag
        self.source=source
        self.extended_hours=extended_hours
        self.legs=legs
        self.trail_percent=trail_percent
        self.trail_price=trail_price
        self.hwm=hwm

class Position:
    def __init__(self,  
        asset_id,
        symbol,
        exchange,
        asset_class, 
        avg_entry_price, 
        qty,
        qty_available,
        side,
        market_value,
        cost_basis,
        unrealized_pl,
        unrealized_plpc,
        unrealized_intraday_pl,
        unrealized_intraday_plpc,
        current_price,
        lastday_price,
        change_today
    ):

        self.asset_id=asset_id
        self.symbol=symbol
        self.exchange=exchange
        self.asset_class=asset_class
        self.avg_entry_price=avg_entry_price
        self.qty=qty
        self.qty_available=qty_available
        self.side=side
        self.market_value=market_value
        self.cost_basis=cost_basis
        self.unrealized_pl=unrealized_pl
        self.unrealized_plpc=unrealized_plpc
        self.unrealized_intraday_pl=unrealized_intraday_pl
        self.unrealized_intraday_plpc=unrealized_intraday_plpc
        self.current_price=current_price
        self.lastday_price=lastday_price
        self.change_today=change_today

class Asset:    
    
    def __init__(self, 
        id, 
        exchange, 
        symbol, 
        status, 
        tradable,
        marginable,
        shortable,
        easy_to_borrow,
        fractionable,
        **kwargs
    ):
        self.id=id
        self.asset_class=kwargs["class"]
        self.exchange=exchange 
        self.symbol=symbol
        self.status=status
        self.tradable=tradable
        self.marginable=marginable
        self.shortable=shortable
        self.easy_to_borrow=easy_to_borrow
        self.fractionable=fractionable

class Snapshot:
    def __init__(
        self, 
        symbol, 
        latestTrade, 
        latestQuote, 
        minuteBar, 
        dailyBar,
        prevDailyBar
    ):
        
        self.symbol=symbol
        self.latestTrade=Trade(**latestTrade)
        self.latestQuote=Quote(**latestQuote)
        self.minuteBar=Bar(**minuteBar)
        self.dailyBar=Bar(**dailyBar)
        self.prevDailyBar=Bar(**prevDailyBar)

class Trade:
    def __init__(
        self,
        t,
        x,
        p,
        s,
        c,
        i,
        z
    ):
        self.t=t #Timestamp
        self.x=x #Exchange where it happened
        self.p=p #Trade Price
        self.s=s #Trade Size
        self.c=c #Trade Conditions
        self.i=i #Trade Id
        self.z=z #Tape
    
class Quote:
    def __init__(
        self,
        **kwargs
    ):
        self.t=kwargs["t"]
        self.ask_x=kwargs["ax"]
        self.ask_p=kwargs["ap"]
        self.ask_s=kwargs["as"]
        self.bid_x=kwargs["bx"]
        self.bid_p=kwargs["bp"]
        self.bid_s=kwargs["bs"]
        self.c=kwargs["c"]
    
class Bar:
    def __init__(
        self,
        t,
        o,
        h,
        l,
        c,
        v,
        n,
        vw
    ):
        self.t=t
        self.o=o
        self.h=h
        self.l=l
        self.c=c
        self.v=v
        self.n=n
        self.vw=vw