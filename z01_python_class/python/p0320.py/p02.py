class Car :
    count = 0
    def __init__(self,color="white",door = 5,speed=0,tire=4):
        self.color = color
        self.speed = speed
        self.door = door
        self.tire=tire
    def up_speed(self):
        self.speed+=10
    def down_speed(self):
        self.speed-=10
    def stop_speed(self):
        self.speed -= 10

class Ambul_car(Car):
    #Car 클래스의 모든 것을 가져옴
    def siren(self):
        print("싸이렌이 울리는 기능이 추가됩니다.")
        
    def up_speed(self):
        self.speed+=20   #자식 클래스에서 오버라이딩 된 함수
        
    def up_speed2(self):    # 기존 부모 함수를 다시 호출하고 싶을 때
        return super().up_speed()   #부모의 요소를 가져올 때 super()

class FireTruck_car(Car):    
    def water(self):
        print("물을 뿌리는 기능이 추가됩니다.")        
    
        
a1= Ambul_car()
print("현재속도: ", a1.speed)
a1.up_speed() #자식의 오버라이딩 된 함수를 호출
print("현재속도: ",a1.speed)

a1.up_speed2()
print("현재속도: ",a1.speed)

a1.stop_speed()
print("현재속도: ",a1.speed)

print("색깔 : ",a1.color)






