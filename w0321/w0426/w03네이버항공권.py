import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 파일에서 가져오기
with open("flight.html",'r',encoding='utf8') as f: soup = BeautifulSoup(f,'lxml')

# 287개 항공권 조회
flights = soup.find_all("div",{"class":"domestic_Flight__sK0eA"})
print("항공권 갯수: ",len(flights))
print("-"*40)

# 항공사
airline_name = flights[0].find("b",{"class":"airline_name__Tm2wJ"})
print("항공사: ",airline_name.text.strip())
# 출발시간
route_time = flights[0].find("b",{"class":"route_time__-2Z1T"})
print("출발시간: ",route_time.text.strip())
# 도착시간
route_times = flights[0].find_all("b",{"class":"route_time__-2Z1T"})
print("도착시간: ",route_times[1].text.strip())
# 항공사 가격
air_price = flights[0].find("i",{"class":"domestic_num__2roTW"})
print("가격: ",air_price.text.strip())

# for문 287개 출력
# 100,000원 이하만 출력될 수 있게 하시오.
flight2 = soup.find("div",{"class":"domestic_results__yNAgI"})
flight3 = flight2.find_all("div",{"class":"domestic_Flight__sK0eA"})
print("제주 항공권 갯수: ",len(flight3))

air_price2 = int(air_price.text.strip().replace(",",""))
print(air_price2)

# for f in flight3:
#     if air_price2 <= 100000:
#         print(len(f))

for i ,flight in enumerate(flights):

    print("[",(i+1),"번째"")]")
    air_price2 = int(air_price.text.strip().replace(",",""))
    if air_price2 > 100000:
        print("10만원 이상 항공권----")
        continue
    airline_name = flight.find("b",{"class":"airline_name__Tm2wJ"})
    print("항공사: ",airline_name.text.strip())
    route_times = flight.find_all("b",{"class":"route_time__-2Z1T"})
    print("출발시간: ",route_times[0].text.strip())
    print("도착시간: ",route_times[1].text.strip())
    print("가격: ",format(air_price2,',')) #천단위 표시 다시함
    print("-"*40)
# print(soup)