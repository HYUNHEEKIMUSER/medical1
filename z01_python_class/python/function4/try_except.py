# 예외 처리를 하게되면 오류가 발생하게 되어도 프로그램이 종료되지 않음
# 프로그램 구현 중에 잘못된 코드 : 구문 오류
#  런타임 오류: 프로그램 실행 중에 발생하는 오류
while True:
    print("[리스트 출력 프로그램]")
    try :   # 오류가 발생될 것 같은 지점에 바로 except로 넘어감
        num =int(input("숫자를 입력하세요"))
        a_list = [1,2,3,4,5]
        for i in range(num):
            print(a_list[i])
    except :
        print("구문에 오류가 났습니다")
     