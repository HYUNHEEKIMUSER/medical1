import random


# form random import* 로 쓰면 앞에 random 안 붙이고 쓸 수 있음 ex)print(uniform(10,20))

print(random.random())   # 0 이하의 랜덤 float 나옴

print(random.uniform(10,20)) # 10~20사이의 랜덤 float 소수점의 결과값을 리턴

print(random.randrange(3))  #0~2까지의 랜덤숫자 리턴

print(random.choice([1,2,3,4,5])) # 리스트 내 랜덤 선택
print(random.sample([1,2,4,5,6],k=4))  #k개 랜덤 선택

a_list =[1,2,3,4,5]
random.shuffle(a_list) # 리스트 내 랜덤으로 섞음
print(a_list)

print(random.randint(1,10)) #1-10에서 범위 내 랜덤 int를 1개 선택




