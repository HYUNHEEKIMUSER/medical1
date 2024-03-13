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
    result1=num1+num2
    result2=num1-num2
    result3=num1*num2
    result4=num1/num2 
    return result1,result2,result3,result4

result1,result2,result3,result4 = cal(num1,num2)
print('{},{} 결과값: {}'.format(num1,num2,result1,result2,result3,result4))