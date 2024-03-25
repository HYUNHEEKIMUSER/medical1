import random
card_list= []
shape = ["spade",'diamond','heart','clover']
num = [0]*13
for i in range(1,14):
    num[i-1]=i
num[0]='A'
num[10]='J'
num[11]='Q'
num[12]='K'

card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape:
    for j in range(13):
        card_list[cnt] = [i,num[j]]
        cnt+=1
        
random.shuffle(card_list)

arr_num = 0
while True:
    print("1.카드 1장 뽑기")
    print("2.카드 5장 뽑기")
    print("0.종료")
    print("현재 남은 카드: ",len(card_list)-arr_num)
    c_num =int(input("번호 선택을 해주세요"))
    if c_num ==1:
        print(card_list[arr_num])
        arr_num +=1
    elif c_num ==2:
        for i in range(5):
            print(card_list[arr_num])
            arr_num+=1
    print(card_list)