#  Car 클래스를 선언
class Car:
    color =""    
    door = ""     
    tire= ""   
    speed=0
    carCount = 0    #클래스 변수
    carNo=1
    
    def __init__(self,color,door,tire,speed):
        self.color=color
        self.door=door
        self.tire=tire
        self.speed =speed
        Car.carCount+=1
        self.carNo=Car.carCount
        
    # upspeed 함수 호출 시 10씩 증가 
    def up_speed(self,speed):
        self.speed+=speed
    # downspeed 함수 호출 시 10씩 감소    
    def down_speed(self,speed):
        self.speed-=speed
        
c1 = Car("white","5","4",0)
for i in range(3):
    c1.up_speed(10)
print(f"1 번째 차 사양: {c1.carNo},{c1.color},{c1.door},{c1.tire},{c1.speed}")
c1_change=(f"1 번째 차 사양: {c1.carNo},{c1.color},{c1.door},{c1.tire},{c1.speed}")

c2 = Car("red","5","4",0)
for i in range(10):
    c2.up_speed(10)
print(f"2 번쨰 차 사양: {c2.carNo},{c2.color},{c2.door},{c2.tire},{c2.speed}")
c2_change=(f"2 번쨰 차 사양: {c2.carNo},{c2.color},{c2.door},{c2.tire},{c2.speed}")

c3 = Car("silver","5","4",0)
for i in range(7):
    c3.up_speed(10)
print(f"3 번째 차 사양: {c3.carNo},{c3.color},{c3.door},{c3.tire},{c3.speed}")
c3_change=(f"3 번째 차 사양: {c3.carNo},{c3.color},{c3.door},{c3.tire},{c3.speed}")

car_list =[]
car_list.append(c1_change)        
car_list.append(c2_change)
car_list.append(c3_change)
print(car_list)