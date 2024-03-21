# 함수선언 def 이름()
# 함수값은 return
# 함수호출 이름()
# 매개변수 개수는 항상 같아야 한다.
# 가변매개변수는 일치하지 않아도 된다.
# 매개변수 : 함수로 데이터 전달하는 변수, 매개변수 개수는 항상 같아야 한다.
# 리스트, 딕셔너리는 주소값이 전달이 된다.

# # 퀴즈
# # 함수를 사용하며 두 수를 입력받아 더하기 빼기 곱하기 나누기 결과값을 출력하시오

# def cal(num1,c,num2): 
#     if c == '+':
#         result=num1+num2
#     elif c== '-':
#         result=num1-num2
#     elif c=='*':
#         result=num1*num2
#     elif c== '/':
#         result=num1/num2 
#     return result
        
# num1 = int(input("1번째 숫자를 입력하세요 >>"))
# c= input("원하는 사칙연산 입력하세요")     
# num2 = int(input("2번째 숫자를 입력하세요 >>"))  
# result = cal(num1,c,num2)
# print('{},{} 결과값: {}'.format(num1,num2,result))

# ---------------------------------- 선생님 답

def cal(num1,num2): 
    r_list = [0]*6
    r_list [0]= num1
    r_list[1] =num2
    r_list[2]=num1+num2
    r_list[3]=num1-num2
    r_list[4]=num1*num2
    r_list[5]=num1/num2 
    return r_list
 
save_list = []

while True:
    num1 = int(input("1번째 숫자를 입력하세요 >> (0번 종료)"))  
    if num1 == 0:
        break
    num2 = int(input("2번째 숫자를 입력하세요 >> "))  
    r_list = cal(num1,num2)
    # save_list에 r_list 저장
    for i in r_list:
        for j in save_list:
            save_list=r_list[i][j]   
    print(r_list)
    
    print('{},{} 결과값: {}'.format(*r_list))

# 현재까지 입력한 숫자와 결과값을 모두 출력해보세요
if num1 == 0:
    print("[현재까지 입력한 숫자: {}, 결과값: {}]".format(r_list[i],save_list))
    
# ---------------------------------------------------선생님 답
# 함수선언 def 이름()
# 함수값은 return
# 함수호출 이름()
# 매개변수 개수는 항상 같아야 한다.
# 가변매개변수는 일치하지 않아도 된다.
# 매개변수 : 함수로 데이터 전달하는 변수, 매개변수 개수는 항상 같아야 한다.
# 리스트, 딕셔너리는 주소값이 전달이 된다.

# 퀴즈
# 함수를 사용하며 두 수를 입력받아 더하기 빼기 곱하기 나누기 결과값을 출력하시오

def cal(num1,c,num2): 
    if c == '+':
        result=num1+num2
    elif c== '-':
        result=num1-num2
    elif c=='*':
        result=num1*num2
    elif c== '/':
        result=num1/num2 
    return result
        
num1 = int(input("1번째 숫자를 입력하세요 >>"))
c= input("원하는 사칙연산 입력하세요")     
num2 = int(input("2번째 숫자를 입력하세요 >>"))  
result = cal(num1,c,num2)
print('{},{} 결과값: {}'.format(num1,num2,result))

# ---------------------------------- 선생님 답

def cal(num1,num2): 
    r_list = [0]*6
    r_list [0]= num1
    r_list[1] =num2
    r_list[2]=num1+num2
    r_list[3]=num1-num2
    r_list[4]=num1*num2
    r_list[5]=num1/num2 
    return r_list
save_list = []

while True:
    num1 = int(input("1번째 숫자를 입력하세요 >> (0번 종료)"))  
    if num1 == 0:
        break
    num2 = int(input("2번째 숫자를 입력하세요 >> "))  
    r_list = cal(num1,num2)
    save_list.append(r_list)

for s in save_list:
    print("[현재까지 입력한 숫자: {}, 결과값: {}]".format(*s))