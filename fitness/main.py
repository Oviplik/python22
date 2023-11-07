from datetime import datetime, timedelta
import calendar

date = datetime.now()
days_in_month = calendar.monthrange(date.year, date.month)[1]
date += timedelta(days=days_in_month)
print(date)