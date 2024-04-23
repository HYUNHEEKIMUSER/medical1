import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')

officeCard=soup.find("div",{"class":"_officeCard _officeCard0"})
ranks = officeCard.find_all("div",{"class":"rankingnews_box"})
print("갯수 : ",len(ranks))

for rank in ranks:
    lis = rank.find_all("li")
    print("제목: ",lis[0].find("a",{"class":"list_title"}).text)
    print("li의 갯수: ",len(lis))
    print("-"*40)




browser = webdriver.Chrome()

# 브라우저 페이지를 열기
browser.get(url)
soup = BeautifulSoup(browser.page_source,'lxml')

res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')








# all = soup.find("ul",{"class":"rankingnews_list"})
# all_find=all.find_all("li")
# content = all_find.find("em",{"class":"list_ranking_num"})
# title = all_find.find("a",{"class":"list_title nclicks"})
# # image= all_find.find("")

# print("1. 목록: ",content)
# print("2. 제목: ",title)
# # print("3. 이미지: ",image)
