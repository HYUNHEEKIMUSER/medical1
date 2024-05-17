import random 

# 클래스 선언 = 설계도
class Card:
    def __init__ (self,kind,number):
        self.kind = kind
        self.number=number
        
# 52장의 카드
# spade, diamond, haert, clover
# 1,2,3,4,5,6,7,8,9,10,11,12,13
kind_list = ['spade', 'diamond', 'haert', 'clover']
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_list = []
# 랜덤 함수
def random_one():
    num = random.randint(0,51)
    print("랜덤카드 1장: ",num,card_list[num].kind,card_list[num].number)
    return card_list    # 랜덤카드 5장 뽑을 때 3번에 쓰려고 씀
# 52장의 카드 생성
for i in range(4):
    for j in range(13):
        card_list.append(Card(kind_list[i],number_list[j]))
# 52장의 카드 출력
for i in range(52):
    print("카드 : ",card_list[i].kind, card_list[i].number)
    
# 랜덤으로 1장 뽑기 출력   
random_one()

# 중복이 되지 않게 랜덤카드 5장을 뽑으시오 
# 1. 51장을 순차적으로 랜덤 섞기 후 순차적으로 뽑기
random.shuffle(card_list)
for i in range(5):
    print("랜덤섞기 카드 : ",card_list[i].kind,card_list[i].number)
# 2. 5장을 랜덤으로 뽑기
ran_list=random.sample(card_list,5)
for i in ran_list:
    print("랜덤sample 카드 : ",i.kind,i.number)
# 3. 1장을 뽑고 기존에 있는 카드와 비교하여 다시 뽑기
temp_list = []
cnt = 0
while True:
    if cnt == 5: break # 랜덤뽑기 카드가 5장일경우 종료
    c = random_one() # 랜덤카드 1장을 뽑기
    for i in temp_list:
        if c.kind == i.kind and c.number == i.number: # 같은 카드가 있으면 다음으로 진행
            continue
    # 중복카드가 없으면 추가
    temp_list.append(c)
    cnt += 1
for i in temp_list:
    print("랜덤1장 뽑기 카드 : ",i.kind,i.number)

