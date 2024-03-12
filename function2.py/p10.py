import random
card =[]
def card_creat(card):
    print('1.카드생성')
    # 카드종류
    card =[]
    card_shape = ["SPADE","DIAMOND","HEART","CLOVER"]
    card_number = [0]*13
    # 카드숫자
    for i in range(13):
        card_number[i]=i
    card_number[0] = "A"
    card_number[-3]="J"
    card_number[-2]="Q"
    card_number[-1]="K"
    # 카드 총 수
    card = [[0]*2 for i in range(52)]
    cnt =0
    for i in card_shape:
        for j in range(13):
            card[cnt]=[i,card_number[j]]
            cnt+=1
    print(card)
    return card
    
def card_shuffle():
    print("2.카드섞기")
    random.shuffle(card_creat(card))
    print(card)
def card_share():
    pass

def card_print():
    pass

while True:
    print("1.카드생성")
    print("2.카드섞기")
    print("3.카드5장 나눠주기")
    print("4.카드5장 확인하기")
    choice = int(input("원하는 번호를 입력하세요 >>"))

    if choice == 1:
        card_creat(card)
    elif choice == 2:
        card_shuffle()
    elif choice ==3:
        card_share()
    elif choice == 4:
        card_print()
    else:
        print("프로그램을 종료합니다0")
        break