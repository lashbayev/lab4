from datetime import datetime
current = datetime.now()
new_current = current.replace(microsecond = 0)
print(new_current)