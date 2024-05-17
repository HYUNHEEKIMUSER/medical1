class Student:
    name= ""
    total = 0
    def __init__(self,name="",total=0):
        self.name=name
        self.__total=total    #클래너 내부에서만 접근
    
    def __str__(self):
        return f"이름:{self.name}, 합계: {self.__total}" #원래 total을 지켜줌(95점)
# 프라이빗 변수    
    def set_total(self,total,login_id):
        if login_id == 'admin':
            self.__total = total
        # 조건을 걸어 데이터 접근을 막는 것
        else:
            print("admin 관리자가 아니면 수정이 불가능하다.")

    def get_total(self):
        return self.__total
  
    def __gt__ (self,s):
        return self.total > s.total
    def stu_print(self):
        print("학생성적 출력합니다")

s=Student("홍길동",95)
s2=Student("유관순",100)

s.total=300
s.set_total(400,"aaa")
print(s.total)
print(s)
print(s.get_total())
# print(s)
# print(s2)
# print(s.total>s2.total) #gt 없을 때
# print(s>s2)  #gt 있을 때