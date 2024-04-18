# 클래스 내에서 함수는 self를 넣어줘야 한다.
class Car:
    car_name = ""
    color = ""
    door = 0
    length = 0
    width = 0
    speed = 0
    
    def up_speed(self,s):
        self.speed += s 
    
c1 = Car()
c1.car_name = "드뉴아반떼"
c1.color = "white"
c1.door = 5
c1.length = 2000
c1.width = 1000
c1.up_speed(60)  #기존의 속도에 더해서 넣어줌
c1.up_speed(40)  # 100
c1.speed = 50 # 현재 스피드 50

c2 = Car()
c2.car_name = "드뉴아반떼"
c2.color = "green"
c2.door = 5
c2.length = 2000
c2.width = 1000
c2.up_speed(100)  

c3 = Car()
c3.car_name = "디올뉴그랜저"
c3.color = "화이트펄"
c3.door = 5
c3.length = 2500
c3.width = 1400
c3.up_speed(150)

print("철수 성능: ", c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)
print("영희 성능: ", c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)
print("반장 성능: ", c3.car_name,c3.color,c3.door,c3.length,c3.width,c3.speed)




           
# c1 = Car
# c1.color = "red"
# c1.speed = 60

# print("차 성능: ", c1.color,c1.door,c1.length,c1.width,c1.speed)

# # 드뉴아반뗴의 차를 1대 생산해서, 색상은 green, 나머지 동일, speed =100 출력 
# c2 = Car
# c2.color = "green"
# c2.speed = 100
# print("드뉴아반뗴 성능 : ",c2.color,c2.door,c2.length,c2.width,c2.speed)

# # 디올뉴그랜저,화이트펄,speed=150,width=1400 length=2500
# c3 =Car
# c3.color = "화이트펄"
# c3.speed = 150
# c3.length= 2500
# c3.width = 1400
# print("디올뉴그랜저 성능 : ",c3.color,c3.door,c3.length,c3.width,c3.speed)
