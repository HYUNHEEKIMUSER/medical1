#  Car 클래스를 선언
class Car:
    color =""    
    door = ""     
    tire= ""   
    speed=0
    carCount = 1    #클래스 변수
    carNo=1

    # upspeed 함수 호출 시 10씩 증가 
    def up_speed(self,speed):
        self.speed+=10
    # downspeed 함수 호출 시 10씩 감소    
    def down_speed(self,speed):
        self.speed-=10
        
c1 = Car("white","5","4",0)
c1.up_speed(30)
print(f"차 사양: {c1.color},{c1.door},{c1.tire},{c1.speed}")
c2 = Car("red","5","4",0)
c2.up_speed(100)
print(f"차 사양: {c2.color},{c2.door},{c2.tire},{c2.speed}")
c3 = Car("silver","5","4",0)
c3.up_speed(79) 
print(f"차 사양: {c3.color},{c3.door},{c3.tire},{c3.speed}")

car_list =[]
car_list.append()        
car_list.append()
car_list.append()