import datetime
now = datetime.datetime.now()
h = now.hour

if h < 12 :
    print('현재는 {}시로 오전입니다.'.format(h))
else :
    print("현재는 {}시로 오후입니다.".format(h))
    
m = now.month

if m % 2 == 0 :
    print("짝수달")
else :
    print("홀수달")
    
m = now.month
if 3 <= m <= 11 :
    print("겨울아님")
else :
    print("겨울") 