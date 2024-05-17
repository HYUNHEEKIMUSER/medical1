# 1번
class Student:
    stuCount= 0   #클래스변수
    stuNo= 0    #인스턴스 변수 (개체 변수 설정할 때마다 데이터 값이 달라지는 것)

# 생성자: __init__
# 클래스에 대해 객체선언을 하면 제일 먼저 호출되는 함수
# 2번
    def __init__(self,name="",kor=0,eng=0,math=0):   
        self.name = name
        if kor >100:
           self.kor=100
        else:
            self.kor=kor
        self.eng = eng
        self.math = math
        self.total=kor+eng+math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = 0
        Student.stuCount +=1 # 자동으로 숫자 증가
        self.stuNo = Student.stuCount
# 3번 
    def stu_print(self):
        print(self.stuNo,self.name,self.kor,self.eng,self.math\
              ,self.total,self.avg,self.rank,sep= '\t')
# 4번
    # 객체를 print하면 __str__함수를 제일 먼저 호출함
    def __str__(self):
        return f"{self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"

        
# 매개변수가 있는 객체(인스턴스)선언 
# 2번
s1 = Student("홍길동",100,100,99)
s2 = Student("유관순",99,99,98)
# 3번
s1.stu_print()
s2.stu_print()
# 4번
print(s1)   #__str__함수호출, 없으면 주소값 출력



