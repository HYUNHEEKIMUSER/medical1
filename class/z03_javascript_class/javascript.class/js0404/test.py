season3=input("월을 입력하세요")
print(season3)
season2=season3[0:-1]
print(season2)

season=int(season2)

if 3>= season<=5:
    print("좀")
elif 6<=season<=8:
    print("여름")
elif 9<=season<=11:
    print("가을")
elif season==12 or 1<=season<=2:
    print("겨울")