#  함수선언

def cal (num1,num2):
    sum = 0
    temp = 0
    if num1>num2:
        num1,num2 = num2,num1   # 1. 큰 수 작은 수 섞여도 되는 것
        temp = num1
        num1 = num2                            #or 2. 이 방법도 있음 
        num2 = temp
    for i in range(num1,num2+1):
        sum +=i
    return sum

# 두 수를 입력받아, 입력한 사이의 합계를 구하는 프로그램을 구현해라
sum =0
num1 = int(input("1번째 숫자 >>"))
num2 = int(input("2번째 숫자 >>"))
sum = cal (num1,num2)
print("합계:  ",sum)












    
