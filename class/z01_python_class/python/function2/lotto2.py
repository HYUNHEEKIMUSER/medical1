import random
def screen():
    print("[로또번호 및 맞추기 프로그램]")
    print("[1. 번호생성]")
    print("[2. 번호섞기]")
    print("[3. 나의로또번호입력]")
    print("[3. 로또당첨번호뽑기]")
    print("[4. 번호확인]")
    print('-'*30)
    choice = int(input("원하는 번호를 입력하세요 >>"))
    return choice
lotto=[0]*45
my_lotto=[0]*6
lucky_lotto = [0]*6   #당첨번호 6개
win_num =[]   # 당첨번호 겹친 것
win_amount =[0,0,1000,10000,100000,1000000,10000000]

# 번호 생성 함수
def num_generation(lotto):
    print('[번호 생성]')
    for i in range(45):
        lotto[i] = i+1
    print(lotto)
    
# 번호 섞기 함수
def num_shuffle(lotto):
    print("[번호 섞기]")
    random.shuffle(lotto)
    print(lotto)

# 나의로또번호입력
def num_my_num(my_lotto):
    print("[나의로또번호입력]")
    for i in range(6):
        my_num = int(input(f"{i+1}번째 로또 번호를 입력하세요 >> "))
        my_lotto[i]=my_num
    print("내가 입력한 번호: ",my_lotto)

# 로또당첨번호뽑기
def num_lucky_lotto(lotto,lucky_lotto,my_lotto,win_num,win_amount):
    print("[번호확인]")
    for i in range(6):
        lucky_lotto[i]=lotto[i]
    print("-"*50)
    print("[번호확인]")
    print("[로또번호: ",lucky_lotto)
    print("내가 입력한 번호: ", my_lotto)
    
# 몇개 맞췄는 지 확인 소스
for i in my_lotto: 
    if i in lucky_lotto:
        win_num.append(i)
print("당첨된 번호: ",win_num)
# 당첨금액 출력
print("당첨금액 : {:,d} 원".format(win_amount[len(win_num)]))
print('-'*40)
print()
