import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# print(soup)
s_all = soup.find("div",{"class":"box_type_l"})
tr_list = s_all.find_all("tr")
print(len(tr_list))
samsung = tr_list[2]
td_list = samsung.find_all("td")
print("-"*40)
print("순위 : ",td_list[0].text)
print("종목명 : ",td_list[1].find("a").text)
print("검색비율 : ",td_list[2].text)
print("현재가 : ",td_list[3].text)
print("ROE : ",td_list[-1].text)
print("PER : ",td_list[-2].text)

print("-"*40)
hanhwa = tr_list[3]
td_list1 =hanhwa.find_all("td")
print("순위 : ",td_list1[0].text)
print("종목명 : ",td_list1[1].find("a").text)
print("검색비율 : ",td_list1[2].text)
print("현재가 : ",td_list1[3].text)
print("ROE : ",td_list1[-1].text)
print("PER : ",td_list1[-2].text)

print("-"*40)
naver = tr_list[4]
td_list2 =naver.find_all("td")
print("순위 : ",td_list2[0].text)
print("종목명 : ",td_list2[1].find("a").text)
print("검색비율 : ",td_list2[2].text)
print("현재가 : ",td_list2[3].text)
print("ROE : ",td_list2[-1].text)
print("PER : ",td_list2[-2].text)

print("-"*40)
samhyun = tr_list[5]
td_list3 =samhyun.find_all("td")
print("순위 : ",td_list3[0].text)
print("종목명 : ",td_list3[1].find("a").text)
print("검색비율 : ",td_list3[2].text)
print("현재가 : ",td_list3[3].text)
print("ROE : ",td_list3[-1].text)
print("PER : ",td_list3[-2].text)

print("-"*40)
echopro = tr_list[6]
td_list4 =echopro.find_all("td")
print("순위 : ",td_list4[0].text)
print("종목명 : ",td_list4[1].find("a").text)
print("검색비율 : ",td_list4[2].text)
print("현재가 : ",td_list4[3].text)
print("ROE : ",td_list4[-1].text)
print("PER : ",td_list4[-2].text)

print("-"*40)
for i in range(2,7):    
    stock = tr_list[i]
    td_list = samsung.find_all("td")
    print("순위 : ",td_list[0].text)
    print("종목명 : ",td_list[1].find("a").text)
    print("검색비율 : ",td_list[2].text)
    print("현재가 : ",td_list[3].text)
    print("ROE : ",td_list[-1].text)
    print("PER : ",td_list[-2].text)

# list 중간 blank 건너 뛰는 법
print("-"*40)
for i in range(2,14):
    stock = tr_list[i]
    td_list = stock.find_all("td")
    if len(td_list)<=1:
        continue
    print("종목명 : ",td_list[1].find("a").text)
    print("검색비율 : ",td_list[2].text)
    print("현재가 : ",td_list[3].text)
    print("ROE : ",td_list[-1].text)
    print("PER : ",td_list[-2].text)
    
