class Student:
    def __init(self,name=""):
        pass
    def stu_print(self):
        print("학생성적 출력합니다")

class Lotto:
    pass

def s_print():
    
    print("class 밖에 있는 함수")
s=Student() 
s2 = Lotto()  

s.stu_print() #클래스 내에 있는 함수는 꼭 객체 선언을 해야 사용가능
if isinstance(s2,Student):
    print("Student 클래스 변수입니다")
elif isinstance(s2,Lotto):
    print("lotto 클래스 변수입니다.")
print(type(s2))
s_print()

