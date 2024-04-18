import co

coffee = 0
# 함수정의 : def 이름 ()


while True: 
    print("1.보통커피")
    print("2.설탕커피")
    print("3.블랙커피")
    coffee = int(input("어떤 커피를 드릴까요?"))
    print()
# 함수사용
    co.machine(coffee)
    