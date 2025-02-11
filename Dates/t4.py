from datetime import datetime

date1 = datetime(2025, 2, 11, 12, 30, 0)  
date2 = datetime(2025, 2, 12, 14, 45, 0)  

difference = date2 - date1

seconds_difference = difference.total_seconds()

print(f"The difference between the two dates is {seconds_difference} seconds.")
