import requests


# 웹 크롤링 형태 
res=requests.get("https://www.naver.com/")
res.raise_for_status()    # 에러코드면 자동 멈춤
print(type(res.text))
print("총 문자길이: ",len(res.text))
# ------------------------------------------------------
#구글 파일 저장하는 법
with open("google.html","w",encoding='utf8') as f:
    f.write(res.text)   