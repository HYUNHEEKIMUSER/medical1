# 번호생성, 번호 섞기, 번호 뽑기, 번호확인
import lotto2

lotto=[0]*45
my_lotto=[0]*6
lucky_lotto = [0]*6   #당첨번호 6개
win_num =[]   # 당첨번호 겹친 것
win_amount =[0,0,1000,10000,100000,1000000,10000000]

while True:
    choice = lotto2.screen()
    
    if choice == 1:
       lotto2. num_generation(lotto)       
        
    elif choice == 2:
        lotto2.num_shuffle(lotto) 
        
    elif choice==3:
        lotto2.num_my_num(my_lotto)
        
    elif choice ==4:
        win_num =[]
        lotto2.num_lucky_lotto(lotto,lucky_lotto,my_lotto,win_num,win_amount)
        win_num =[]
        # 몇개 맞췄는 지 확인 소스
        
    elif choice == 5:
        correct = []
        for i in range(len(my_lotto)): 
            if my_lotto[i] in lucky_lotto:
                correct.append(my_lotto[i])
        print(correct)
        
# 몇개 맞췄는 지 확인 소스

    for i in my_lotto: 
        if i in lucky_lotto:
            win_num.append(i)
    print("당첨된 번호: ",win_num)
# 당첨금액 출력

    print("당첨금액 : {:,d} 원".format(win_amount[len(win_num)]))
    print('-'*40)
    print()