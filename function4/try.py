# 외부와의 데이터 전송, 데이터 받기, 외부기기 연결, 다른 프로그램 연결 
# 이런 것 외에는 되도록 프로그램이 오류 발생되지 않도록 하는게 가장 좋다.
print("프로그램 실행")
try:
    print(1)
    print(2)
    print(3)
    print(1/0) #에러발생  #에러 발생하고 except에서 다시 실행 try 문이 없으면 1,2에서 멈춤
    print(4)
except:
    print(5)
print(6)
print("프로그램 종료")
