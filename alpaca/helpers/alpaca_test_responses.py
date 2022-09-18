sample_test_account = {
        'id': 'dc2d94ce-05fd-40c0-aa7d-186cf63a253f', 
        'account_number': 'PA3TTDISW3W5', 
        'status': 'ACTIVE', 
        'crypto_status': 'ACTIVE', 
        'currency': 'USD', 
        'buying_power': '200040.02', 
        'regt_buying_power': '200040.02', 
        'daytrading_buying_power': '0', 
        'non_marginable_buying_power': '100020.01', 
        'cash': '100020.01', 
        'accrued_fees': '0', 
        'pending_transfer_in': '0', 
        'portfolio_value': '100020.01', 
        'pattern_day_trader': False, 
        'trading_blocked': False, 
        'transfers_blocked': False, 
        'account_blocked': False, 
        'created_at': '2022-08-27T18:11:45.395698Z', 
        'trade_suspended_by_user': False, 
        'multiplier': '2', 
        'shorting_enabled': True, 
        'equity': '100020.01', 
        'last_equity': '100020.01', 
        'long_market_value': '0', 
        'short_market_value': '0', 
        'initial_margin': '0', 
        'maintenance_margin': '0', 
        'last_maintenance_margin': '0', 
        'sma': '100020.01', 
        'daytrade_count': 0
    }

sample_test_order = [{'id': '1d381bef-6ddc-4213-812b-cf1416fb2e5b', 'client_order_id': '601365b7-1b99-457d-af8a-8d1d83ce92a7', 'created_at': '2022-09-18T18:29:25.67651Z', 'updated_at': '2022-09-18T18:29:25.67651Z', 'submitted_at': '2022-09-18T18:29:25.675433Z', 'filled_at': None, 'expired_at': None, 'canceled_at': None, 'failed_at': None, 'replaced_at': None, 'replaced_by': None, 'replaces': None, 'asset_id': 'b0b6dd9d-8b9b-48a9-ba46-b9d54906e415', 'symbol': 'AAPL', 'asset_class': 'us_equity', 'notional': None, 'qty': '1', 'filled_qty': '0', 'filled_avg_price': None, 'order_class': '', 'order_type': 'market', 'type': 'market', 'side': 'buy', 'time_in_force': 'day', 'limit_price': None, 'stop_price': None, 'status': 'accepted', 'extended_hours': False, 'legs': None, 'trail_percent': None, 'trail_price': None, 'hwm': None, 'subtag': None, 'source': 'access_key'}, {'id': '312714de-57fe-4548-9a73-7adfbcc6f7a3', 'client_order_id': '55fa1084-1919-4d8d-90fd-da22bf71e328', 'created_at': '2022-09-18T18:26:23.039717Z', 'updated_at': '2022-09-18T18:26:23.039717Z', 'submitted_at': '2022-09-18T18:26:23.038853Z', 'filled_at': None, 'expired_at': None, 'canceled_at': None, 'failed_at': None, 'replaced_at': None, 'replaced_by': None, 'replaces': None, 'asset_id': 'b28f4066-5c6d-479b-a2af-85dc1a8f16fb', 'symbol': 'SPY', 'asset_class': 'us_equity', 'notional': None, 'qty': '1', 'filled_qty': '0', 'filled_avg_price': None, 'order_class': '', 'order_type': 'market', 'type': 'market', 'side': 'buy', 'time_in_force': 'day', 'limit_price': None, 'stop_price': None, 'status': 'accepted', 'extended_hours': False, 'legs': None, 'trail_percent': None, 'trail_price': None, 'hwm': None, 'subtag': None, 'source': 'access_key'}]

sample_test_historicalBar = {
    'symbol': 'GOOG', 
    'latestTrade': {'t': '2022-09-16T19:59:59.461566836Z', 'x': 'V', 'p': 103.55, 's': 200, 'c': ['@'], 'i': 15401, 'z': 'C'}, 
    'latestQuote': {'t': '2022-09-16T20:00:00.000660247Z', 'ax': 'V', 'ap': 0, 'as': 0, 'bx': 'V', 'bp': 0, 'bs': 0, 'c': ['R'], 'z': 'C'}, 
    'minuteBar': {'t': '2022-09-16T19:59:00Z', 'o': 103.77, 'h': 103.77, 'l': 103.55, 'c': 103.55, 'v': 26275, 'n': 247, 'vw': 103.660876}, 
    'dailyBar': {'t': '2022-09-16T04:00:00Z', 'o': 102.85, 'h': 104.02, 'l': 101.92, 'c': 103.55, 'v': 1225998, 'n': 15409, 'vw': 103.149099}, 
    'prevDailyBar': {'t': '2022-09-15T04:00:00Z', 'o': 104.995, 'h': 106.18, 'l': 103.32, 'c': 103.89, 'v': 938462, 'n': 10441, 'vw': 104.38748}}

sample_test_historicalBars = {'AAPL': {'latestTrade': {'t': '2022-09-16T19:59:59.901959883Z', 'x': 'V', 'p': 150.46, 's': 400, 'c': ['@'], 'i': 21113, 'z': 'C'}, 'latestQuote': {'t': '2022-09-16T20:00:48.017824399Z', 'ax': 'V', 'ap': 0, 'as': 0, 'bx': 'V', 'bp': 0, 'bs': 0, 'c': ['R'], 'z': 'C'}, 'minuteBar': {'t': '2022-09-16T19:59:00Z', 'o': 150.87, 'h': 150.91, 'l': 150.42, 'c': 150.45, 'v': 67069, 'n': 381, 'vw': 150.731263}, 'dailyBar': {'t': '2022-09-16T04:00:00Z', 'o': 151.18, 'h': 151.35, 'l': 148.405, 'c': 150.46, 'v': 2699287, 'n': 21113, 'vw': 149.900337}, 'prevDailyBar': {'t': '2022-09-15T04:00:00Z', 'o': 154.755, 'h': 155.23, 'l': 151.39, 'c': 152.365, 'v': 1877769, 'n': 16650, 'vw': 152.938516}}, 'GOOG': {'latestTrade': {'t': '2022-09-16T19:59:59.461566836Z', 'x': 'V', 'p': 103.55, 's': 200, 'c': ['@'], 'i': 15401, 'z': 'C'}, 'latestQuote': {'t': '2022-09-16T20:00:00.000660247Z', 'ax': 'V', 'ap': 0, 'as': 0, 'bx': 'V', 'bp': 0, 'bs': 0, 'c': ['R'], 'z': 'C'}, 'minuteBar': {'t': '2022-09-16T19:59:00Z', 'o': 103.77, 'h': 103.77, 'l': 103.55, 'c': 103.55, 'v': 26275, 'n': 247, 'vw': 103.660876}, 'dailyBar': {'t': '2022-09-16T04:00:00Z', 'o': 102.85, 'h': 104.02, 'l': 101.92, 'c': 103.55, 'v': 1225998, 'n': 15409, 'vw': 103.149099}, 'prevDailyBar': {'t': '2022-09-15T04:00:00Z', 'o': 104.995, 'h': 106.18, 'l': 103.32, 'c': 103.89, 'v': 938462, 'n': 10441, 'vw': 104.38748}}}

sample_asset = {'id': 'b28f4066-5c6d-479b-a2af-85dc1a8f16fb', 'class': 'us_equity', 'exchange': 'ARCA', 'symbol': 'SPY', 'name': 'SPDR S&P 500 ETF Trust', 'status': 'active', 'tradable': True, 'marginable': True, 'maintenance_margin_requirement': 30, 'shortable': True, 'easy_to_borrow': True, 'fractionable': True}
