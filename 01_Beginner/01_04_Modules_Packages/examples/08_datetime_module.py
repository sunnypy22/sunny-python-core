
# 08_datetime_module.py
from datetime import datetime, timedelta
now = datetime.now()
print("Current date & time:", now)
print("Formatted         :", now.strftime("%d-%m-%Y %H:%M:%S"))
future = now + timedelta(days=30)
print("30 days later     :", future.date())