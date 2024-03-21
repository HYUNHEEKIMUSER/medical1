class Card:
    kind = ""
    number = ""
    def __init__(self,kind="",number=""):
        self.kind = kind
        self.number=number
    
    def number_change(self,s):
        self.number+=s
    
c1= Card("spade",1)
list = []
# c1의 숫자를 5로 변경하세요
# c1을 출력하세요

c1 = Card("spade",1)
print(f"카드 : {c1.kind},{c1.number}")
list.append(c1)
print(list)
c1.number_change(4)
print(f"카드 : {c1.kind},{c1.number}")

# c2 "heart","A"
# 모양을 "DIAMOND"로 변경 후 출력

c2 = Card("heart","A")
c2.kind="diamond"

# -----------------
# 리스트를 이용해서 52장의 카드 생성 
c_list = []
kind = ["spade","diamond","heart","clover"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(4):
    for j in range(13):
        c = [kind[i],number[j]]
        c_list.append(c)        #리스트 생성해서 리스트 추가
        
for i in range(4):
    for j in range(13):
        print("카드 출력 : ",kind[i],number[j])

# 클래스를 이용해서 52장의 카드를 생성
c_list = []
kind = ["spade","diamond","heart","clover"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(4):
    for j in range(13):
        c = Card(kind[i],number[j])  #클래스를 생성하서 리스트에 추가
        c_list.append(c)
for i in range(52):
    print("카드 출력 : ",c_list[i].kind, c_list[i].number)        
        
        
        
        
        
        
        
        
        
        
        