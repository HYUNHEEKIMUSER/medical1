class Student:
    def __init__ (self,name,total):
        self.name = name
        self.total=total
    # def __str__ (self):
    #     return f"이름:{self.name}, 총점: {self.total}"
    def __del__(self):
        return "클래스가 소멸될 때 실행"
    def __add__(self,s):
        return self.total+s.total
    def __gt__(self,s):  #크거나 같다라고 비교할 때
        return self.total > s.total
    def __eq__ (self,s):
        return self.name ==s.name and self.total==s.total
            
# -------------------------------------        
s1 = Student("홍길동",100)
s2 = Student("유관순",90)
s3 = Student("이순신",95)
s4 = Student("홍길동",100)

print(s1)   #클래스를 출력할 때 str 함수 호출
print(s1+s2)   #클래스를 더하기 할 때, add 함수 호출

print(s1>s2)    # 문구가 호출이 됨. 기호를 사용하면(return대신 print 문구 넣으면)
print(s2>s3)
a_list = [10,20,30,40]
b_list = [2,3,4,5]
print(a_list>b_list)

print(s1==s4) # s1과 s4는 같지 않으므로 false라고 나옴 (주소값이 다르므로)
# ->__eq__ 설정하기 전에는 false인데 eq를 설정하면 안의 내용값이 같으므로 
# True 나옴. 
print(s2==s3)