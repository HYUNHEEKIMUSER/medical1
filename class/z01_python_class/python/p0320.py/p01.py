class Car:
    count = 0
    def __init__ (self,color="",speed=0):     #color이렇게 쓰면 ()에 값을 넣어야 됨
        self.color = color   #color =""키워드 변수 설정하면 ()안에 안써도 됨
        self.speed = speed
        # Car.count = 0  #클래스 변수선언
# class 사용하기 위해서는 인스턴스 선언
c1 = Car() #인스턴스 선언
Car.count=200  # 중간에 Car.count=10으로 설정하면 클래스변수도 다같이 변해서 c2도 적용을 받음
print(c1.count)
print(Car.count) 
c1= Car("white")
c1.color ="white" #color="" 설정해놔서
print(c1.color)
c2 = Car()
c2.color = "red"
print(c2.color)
c2.count =200
print(c2.count)


# 클래스 변수로 사용하고 싶다면
# Car.count= 100
# ------------------------------------
print("c1.count: ",c1.count)
print("c2.count: ",c2.count)

c2.door = 4         #class에 설정안했지만 중간에 이렇게 설정해줄 수도 있음 하지만 c2에는 door가 없음(일시적으로)
print(c2.door)
c2.count = 1 # 기존의 클래스변수를 지우고 인스턴스변수를 다시 생성함 이거 없었으면 200 나옴
print(c2.count)
c3 = Car()
print(c3.count)