from datetime import datetime

date1 = datetime(2023, 10, 31, 12, 0, 0)  
date2 = datetime(2023, 11, 1, 12, 0, 0)   

difference = date2 - date1

difference_in_seconds = difference.total_seconds()

print("Difference between the two dates in seconds:", difference_in_seconds)
