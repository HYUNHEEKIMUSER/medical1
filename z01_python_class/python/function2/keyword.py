# 키워드 매개변수
def func2(num1,num2,num3=3): # 키워드 매개변수 num3=3은 값이 없어도 됨.알아서 3으로 됨
    print(num1,num2,num3)
    
func2(1,2)

def func2(num1,num2=100,num3=100):
    print(num1,num2,num3)
    
func2(1)