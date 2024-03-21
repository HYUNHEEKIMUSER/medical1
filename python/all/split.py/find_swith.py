ss = "파이썬 공부는 재밌습니다. 물론 모든 공부가 다 재미있지는 않죠"
print(ss.count("공부")) # 존재하는 문자가 몇 개인지 세어줌, 없으면 0으로 뜸
print(ss.find("공부")) #처음 문자의 위치값이 나타남, 존재하지 않으면 -1로 뜸
print(ss.find("공부",7)) #7이 검색위치, 시작 위치(7번째자리부터)를 다시 설정해서 세어줌
print(ss.rfind("공부")) #오른쪽부터 거꾸로 세어줌
print('-'*35)

print(ss.index("공부")) #find랑 같음.
print(ss.startswith("자바")) # true false 형태 시작하는 문자열에 대한 맞고 틀린 것

print(ss.endswith("않습니다")) # true false 형태 끝나는 문자열에 대한 맞고 틀린 것


 


