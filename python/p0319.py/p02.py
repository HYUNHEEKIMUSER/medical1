class Car:
    color= ""
    door = 5
    tire = 4
    speed =0
    
    def __init__ (self,color,door,tire,speed):
        self.color = color
        self.door = door
        self.tire=tire
        self.__speed = speed # c1.speed =300처럼 갑자기 올라가게 못하게 막음
        # 클래스 내부에서만 접근이 가능하게 만듦
        # self.speed = speed  
    def up_speed(self,smartKey):    #+/-일 때만 쓰는 게 아니라 self옆에 더 붙이고 if 해서 값에 따라 올릴 수 있음
        if smartKey == '0x1100':
            self.__speed += 10
        else : 
            print("스마트키가 다릅니다")
    def down_speed(self):
        self.__speed -= 10
        
    def get_speed(self):
        return self.__speed
    
    def set_speed(self,speed):
        self.__speed += speed

c1 = Car("white",5,4,0)
c1.up_speed("0x1100")
c1.up_speed("0x1111")
c1.set_speed(500)
print(c1.get_speed())  # 클래스 변수에 직접적으로 접근이 안됨 get을 통해서만 접근가능
