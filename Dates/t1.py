from datetime import datetime, timedelta

current_data = datetime.now()
new_data = current_data - timedelta(days = 5)
print(new_data)