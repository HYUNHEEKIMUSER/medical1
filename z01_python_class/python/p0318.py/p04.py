# 키워드 매개변수 (n2=10)
def cal(n1,n2=10):
    n1 = n1+10
    n2 = n2+20
    result = n1+n2
    return result


num1 = 5
num2 = 7

result = cal(num1,num2)
print("현재 숫자: ",num1,num2,result)

# 키워드매개변수는 제일 뒤에 와야함
        
        