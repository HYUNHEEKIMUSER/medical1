# 함수선언
def plus(n1,n2): # def 이름(매개변수1, 매개변수2)
    result = 0
    result = n1 + n2
    print(f'결과값: {result}')
    
print('프로그램을 시행합니다.')
plus(1,2) # 매개변수가 2개면 무조건 2개 들어와야 함 아니면 에러
plus(10,20) # 함수호출:함수이론(매개변수 갯수를 맞추면 됨)

