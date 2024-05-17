

def cal (input1,input2):
    result1=input1+input2
    result2=input1-input2
    result3=input1*input2
    result4=input1/input2
    return result1,result2,result3,result4

input1 = int(input("숫자 입력"))
input2= int(input("2번째 숫자 입력"))

# 함수의 return을 사용하여 입력된 두수의 사칙연산 값을 출력하세요
# 20,10
# 결과값 30,100,200,2

result1,result2,result3,result4=cal(input1,input2)
data = cal(input1,input2)
print("더하기 : ", result1)
print("빼기 : ", result2)
print("곱하기 : ", result3)
print("나누기 : ", result4)
print("결과값 : ",result1,result2,result3,result4) 
print("결과값 : ",data) 
print("결과값 : ",data[0])      





