# split() 문자열 분리
hobby = "게임,골프,독서"

print(hobby.split(","))

h_data = "2023-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합"
print(h_data.split(","))
h_list=h_data.split(",")
print("병상수 : ",h_list[4])

a_data = "2023-10-23/1/강원도 강릉시/강릉동인병원/383/21/033)651-6167/강릉대로419번길 42/종합"
a_list = a_data.split('/')
print("병상수: ",a_list[4])

ss = "%"
print(ss.join("파이썬"))

s_data = "2023/03/08"
s_data_list = s_data.split("/")
print(s_data_list)
s_time= "2023:03:08:16:48:00"
s_time_list = s_time.split(':')
print(s_time_list)

today = "2024/03/08"
# 10년 후의 날짜 출력
s_today=today.split('/')
print(s_today)
date = int(s_today[0])+10,s_today[1],s_today[2]
print("{}/{}/{}".format(*date))