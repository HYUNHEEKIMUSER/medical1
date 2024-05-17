from datetime import datetime

from pytz import timezone

print(datetime.now(timezone('Asia/Seoul')))

now = datetime.now()   # import datetime 한번만 적으면 datetime.datetime으로 적어야됨.
print("시간을 포맷에 맞춰 출력하기")

output_a = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
print(output_a)
output_b = now.strftime("%Y-%m-%d %H:%M:%S")
print(output_b)
# import datetime
# from datetime import datetime

# print("현재시각 출력")
# now = datetime.now()    

# print(now.year,"년")
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시")
# print(now.minute,"분")
# print(now.second,"초")
# print()