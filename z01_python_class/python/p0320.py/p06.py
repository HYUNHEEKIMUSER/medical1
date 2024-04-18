from datetime import datetime
import time
# 시작일
now = datetime.now()
start_time = datetime(now.year,now.month,now.day,now.hour,now.minute,now.second)
print(start_time)
end_time = datetime(2024,6,24)
print(end_time)
print((end_time - now).days)
print(end_time - now)