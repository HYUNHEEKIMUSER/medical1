# 재귀 함수
def count(num):
    if num >=1:
        print(num,end = '')
        count(num-1)
    else: 
        return
count(3)

for i in range(10,0,-1):
    print(i)
    