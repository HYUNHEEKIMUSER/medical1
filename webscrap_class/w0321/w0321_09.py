import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EB%93%B1%EC%B4%8C%EC%A3%BC%EA%B3%B5+%EB%B6%84%EC%96%91"
headers = {"User=Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 등촌주공3단지 매매시세, 전세시세를 출력
apt = soup.find("dl",{"class":"info_price"})
dd_list = apt.find_all("dd")
live=dd_list[0].text
sell=dd_list[1].text
# justlive= dt_list[3]
print("매매시세: ",live)
print("전세시세: ",sell)
# print("전세시세: ",justlive)
# with open('real.html','w',encoding='utf8') as f:  ->메모장 같은 파일
#     f.write(soup.prettify())    
print("종료")

print('-'*40)
# -----------------------------------------------선생님 답
# # 등촌주공3단지 매매시세, 전세시세를 출력
# 등촌 주공 모든 단지 출력
real = soup.find("ol",{"class":"list_place"})
li_list = real.find_all("li")
# print(len(li_list))
for i in range(len(li_list)):
    title = li_list[i].find("div",{"class":"wrap_tit"}).a.text.strip() #공백제거
    print("제목 : ",title)

    dd_list = li_list[i].find_all("dd",{"class":"f_red"})
    # print(len(dd_list))
    print("매매시세: " ,dd_list[0].text)
    print("전세시세: " ,dd_list[1].text)
    print('-'*50)