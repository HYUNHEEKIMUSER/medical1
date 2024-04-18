# 매개변수로 리스트를 사용하는 경우 return은 필요없다.

def func1(a, a_list):
    a = 100
    return a

a = 10
a_list = [1,2,3]
a =func1(a, a_list)
print(a)
print(a, a_list)
# -----------------------------------
def func1(a, a_list):
    a = 100
    pass

a = 10
a_list = [1,2,3]
func1(a, a_list)
print(a)
print(a, a_list)
# -------------------------------------
def func1(a, a_list):
    a = 100
    a_list[0]=100 # 지역변수
    return a

a = 10
a_list = [1,2,3]
a= func1(a, a_list) # 2개이상의 데이터를 저장한느 변수: 주소값을 저장함.

print(a)
print(a, a_list)