# 가변매개변수(*)->리스트 타입으로 받겠다
# 앞에 대문자 클래스 소문자 함수 괄호없으면 변수
def str_title(num,*txt):
    print("txt타입 : ",type(txt))
    print(txt)
    for i in range(num):
        for t in txt:
            print(t, end = ' ')
        print()
    

str_title(1,"안녕","잘가","안녕하세요","반갑습니다")    