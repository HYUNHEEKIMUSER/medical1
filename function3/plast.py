# card =[]
# card_shape = ["SPADE","DIAMOND","HEART","CLOVER"]
# card_number = [0]*13
#     # 카드숫자
# for i in range(13):
#     card_number[i]=i+1
  
# c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]

import random
c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# 랜덤으로 2개의 숫자를 뽑아서 출력하세요
a = random.sample(c_number,k=2)
# 몇 번째 방에 있는 지 출력 ex 랜덤숫자 :2 -> 1번방에 있습니다.
print(a)
print(f"랜덤숫자: {a[0]} -> {[0]}방에 있습니다.")
print(f"랜덤숫자: {a[1]} -> {[1]}방에 있습니다.")
# 큰 수: 작은 수: 뽑아보기
if a[0] > a[1] :
    print(f"큰 수: {a[0]}, 작은 수: {a[1]}")
else:
    print(f"큰 수: {a[1]}, 작은 수: {a[0]}")