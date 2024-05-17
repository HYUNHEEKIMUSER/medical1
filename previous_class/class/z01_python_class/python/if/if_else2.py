a = 97
if a > 90:
    print('a가 90보다 크다')
else :
    print('90보다 작다')

if a > 90:
    print('b')
    if a < 95:
        print('c')
    else :
        print("d")
    
else :
    print('e')
    
apple = "good"
price = 500
if apple == 'good' :
    if price <= 1000 :
        print("10개구매")
    else :
        print("3개구매")
else :
    print("구매 안함")
    
    
num = int(input("숫자"))
if num > 100 :
    if ('num / 2 =={}.format(%f = %0)') :
        print("짝수")
    else : 
        print("홀수")
else : 
    print("100보다 작다")
    
# or num % 2 == 0:

id = 'admin'
pwd = '1111'

uid = input("아이디")
upw = input("비번")

if id == uid :
    if pwd == upw :
        print("일치하여 로그인 되었습니다")
    else :
        print("비밀번호가 일치하지 않습니다")
else :
    print("아이디가 일치하지 않습니다.")
    

    