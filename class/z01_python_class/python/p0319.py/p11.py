import random
card_list=[]
shape = ["spade","diamond","heart","clover"]
num = [0]*13
for i in range(1,13+1):
    num[i-1]=i

num[0]="A"
num[10]='J'
num[11]='Q'
num[12]='K'

card_list = [[0]*2 for i in range(52)]
cnt =0
for i in shape:
    for j in range(13):
        card_list[cnt]=[i,num[j]]
        cnt +=1
        
card_list = [[0]*2 for i in range(52)]
cnt= 0
for i in shape:
    for j in range(13):
        card_list[cnt]=[i,num[j]]
    cnt+=1
    
random.shuffle(card_list)

arr_num = 0
while True:
    print()