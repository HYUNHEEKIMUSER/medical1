import requests
from bs4 import BeautifulSoup

url="https://www.google.com/search?q=%ED%99%98%EC%9C%A8&sca_esv=125395e02bc1fefe&ei=PQsiZourIO7t1e8P0uiDmAk&udm=&ved=0ahUKEwjLvY7Az82FAxXudvUHHVL0AJMQ4dUDCBA&uact=5&oq=%ED%99%98%EC%9C%A8&gs_lp=Egxnd3Mtd2l6LXNlcnAiBu2ZmOycqDILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBBAAGAMyCxAAGIAEGLEDGIMBMg4QABiABBixAxiDARiKBUiuH1DzFVihHnABeAGQAQGYAewBoAHTBqoBBTAuNS4xuAEDyAEA-AEBmAIDoAL1AcICChAAGLADGNYEGEfCAggQABiABBixA8ICCxAuGIAEGLEDGIMBwgIOEC4YgAQYsQMYgwEYigXCAhEQLhiABBixAxjRAxiDARjHAcICBRAAGIAEmAMAiAYBkAYKkgcDMS4yoAeqNg&sclient=gws-wiz-serp"
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

# with open("dollar.html","w",encoding="utf-8") as f:
    #  f.write(res.text)
#해당 태그 출력
print(soup.title.text)

print("미국달러:" ,soup.find("input",{"class":"lWzCpb ZEB7Fb"})["value"])
print("원화: ",soup.find("input",{"class":"lWzCpb a61j6"})["value"])
