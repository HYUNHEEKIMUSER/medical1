def jegob(val):
    return val**2

def func(val):
    return val >=3

def int_change(val):  #=ss_list =list(map(lambda val:int(val),str_list))
    return int(val)   #람다 함수는 이 두 줄을 한 줄로 바꾼 것

a_list = [1,2,3,4,5]
str_list = ['1','2','3','4','5']
map_list = list(map(jegob, a_list))
print(map_list)
# map은 a_list에 있는 것을 jegob으로 하나씩 연결해준 뒤 list에 넣어줌
# 리스트 전체에 값의 변경이 필요할 때 


ss_list = list(map(int_change,str_list))
print(str_list)
print(ss_list)

ss_list2 = list(map(lambda val:int(val),str_list))
print(ss_list2)

f_list = list(filter(func,a_list))
print(f_list)
# 조건에 맞는 값만 추출

