from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(day = 1)
tomorrow = today + timedelta(day = 1)
print(today.strftime('%Y-%m-%d'))
print(yesterday.strftime('%Y-%m-%d'))
print(tomorrow.strftime('%Y-%m-%d'))