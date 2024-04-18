from datetime import datetime
import time
now=datetime.now()
# strftime 특정한 형태로 출력
for i in range(10):
    now=datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)
