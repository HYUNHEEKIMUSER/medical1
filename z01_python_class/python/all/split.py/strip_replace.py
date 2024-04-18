#  strip () ->공백제거를 알아서 해줌 
s1 = " 파이썬 "
s2 = "파이썬"
ss="apple은 당도가 높고, apple의 색상은 빨강, 녹색이 있습니다."

print(s1.lstrip()) # 왼쪽 공백 제거 한 후 print
print(s1.rstrip()) # 오른쪽 공백 제거한 후 print
print(s1.strip()) #양쪽 공백 제거

s_input= input("현재 배우는 과목은 >>").strip()    #뒤에다가 .strip() ->공백있어도 인식
if s_input == s2:
    input("정답입니다")
else: 
    print("오답입니다")



if s1.strip() ==s2:
    print("맞습니다")
else:
    print("틀립니다")
    
print(s1.replace("파","자")) #문자열을 다른 문자 열로 대체
print(s1.replace(" ","")) #만약 파이  썬을 파이썬으로 간격을 줄여주기도 한다

news = "정용진 신세계그룹 총괄부회장이 8일 회장 자리에 올랐다. 2006년 부회장에 오른 후 18년 만에 이뤄진 승진 인사다. 지난해 이마트 창립 이후 적자를 기록했고, 신세계그룹 매출이 감소하는 등 사업 환경이 악화하면서 위기 극복을 위한 새로운 리더십을 내세웠다."
print(news.replace(" ",""))

print(news.replace('그룹','group'))