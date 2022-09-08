import datetime
from dateutil.relativedelta import relativedelta

def subtract_time_from_todays_date(date = datetime.date.today(), year=0, month=0, day=0):
    if isinstance(date, datetime.date):
        return (date + relativedelta(years =- year,months=-month, days=-day))
    else:
        raise(ValueError)