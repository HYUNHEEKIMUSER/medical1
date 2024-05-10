class Card:      #4개의 변수: 클래스 변수
    width = 0
    height = 0
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number=number
        Card.width = 100
        Card.height = 200
        
        
# 52장의 카드 생성
shape = ["SPADE", "DIAMOND", "HEART", 'CLOVER']
number = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
card_list = []
for i in range(4):
    for j in range(13):
        c=Card(shape[i],number[j]) #객체선언
        card_list.append(c)
        
for i in range(52):
    c = card_list[i]
    print("카드출력: ",c.kind, c.number)



