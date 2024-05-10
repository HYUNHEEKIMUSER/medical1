class Card:      #4개의 변수: 클래스 변수
    width = 0
    height = 0
    kind = ""
    number = ""
    shape = ""
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number=number
        Card.width = 100
        Card.height = 200

    def card(self):    #인스턴스함수
        print(f"card : {self.shape},{self.number}")
        
# 클래스 5개를 생성해서 kind = "spade" number = 1,2,3,4,5
# 클래스 출력
shape = ["spade"]
number = [1,2,3,4,5]
card = []

for i in range(13):
    card.append(Card("shape",i+1))

card.append(Card("shape","A"))
card.append(Card("shape","2"))
card.append(Card("shape","3"))
card.append(Card("shape","4"))
card.append(Card("shape","5"))
card.append(Card("shape","6"))
card.append(Card("shape","7"))
card.append(Card("shape","8"))
card.append(Card("shape","9"))
card.append(Card("shape","10"))
card.append(Card("shape","J"))
card.append(Card("shape","Q"))
card.append(Card("shape","K"))
print(len(card))

for i in range(13):
    print(card[i].kind, card[i].number)



