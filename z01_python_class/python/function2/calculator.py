# 두 수를 입력받아 두 수 사이의 합계를 구하시오

# 1 두 수 입력
# 2 함수 호출
# 합계를 return 받아서 합계 : 55 출력
# 지역변수에서 sum이 0으로 설정 안되어 있으면 전역변수에서 sum을 찾아 대체는 된다
# 그런데 계산은 안된다. 대체까지는 된다
# 1~10까지의 합, 빼기, 곱하기의 결과값을 출력할 수 있다.
# 파이썬 언어는 인터프리터 언어, 컴파일러 언어

def cal (s_list):
    for i in range(s_list[0], s_list[1]+1):
        s_list[2] +=i 
        s_list[3] -=i
        s_list[4] *=i
        

num1 = int(input("1번째 숫자를 입력하세요 >"))
num2 = int(input("2번쨰 숫자를 입력하세요 >"))
s_list = [num1, num2, 0,0,1]

cal(s_list)

# 함수호출 리스트로 보내기
list =[]
print("더하기의 결과값 : ", s_list[2])
print("뺴기의 결과값 : ",s_list[3])
print("곱하기의 결과값 : ",s_list[4])


