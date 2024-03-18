# class Student:
#     stuNo = 0
#     stu_name = ""
#     kor = 0
#     eng = 0
#     math = 0
#     total = 0
#     avg = 0
#     rank = 0
    
#     def up_score(self,score):
#         self.score += score
#     def down_score(self,score):
#         self.score -= score
        
#     def students(self,n,na,k,e,m,t,a,r):
#         self.stuNo = n
#         self.stu_name = na
#         self.kor = k
#         self.eng = e
#         self.math = m
#         self.total = t
#         self.avg = a
#         self.rank = r    
# # 1,홍길동,99,99,87,285,95.0,1
# 2,김유신,98,93,87,278,92.67,3
# 3,이순신,88,76,30,194,64.67,6
    
# 홍길동, 김유신, 이순신

# stu_1 = Student(1,'홍길동',99,99,87,285,95.0,1)
# print(f"홍길동 성적: {stu_1.stuNo},{stu_1.stu_name},
#       {stu_1.kor},{stu_1.eng},{stu_1.math},
#       {stu_1.total},{stu_1.avg},{stu_1.rank}")
# stu_2 = Student(2,'김유신',98,93,87,278,92.67,3)
# print(f"김유신 성적: {stu_2.stuNo},{stu_2.stu_name},
#       {stu_2.kor},{stu_2.eng},{stu_2.math},
#       {stu_2.total},{stu_2.avg},{stu_2.rank}")
# stu_3 = Student(3,'이순신',88,76,30,194,64.67,6)
# print(f"이순신 성적: {stu_3.stuNo},{stu_3.stu_name},
#       {stu_3.kor},{stu_3.eng},{stu_3.math},
#       {stu_3.total},{stu_3.avg},{stu_3.rank}")
# -------------------------
class Student:
    stuNo = 0
    stu_name = ""
    kor = 0
    eng = 0
    math = 0
    total = 0
    avg = 0
    rank = 0
    
s1 = Student()
s1.stuNo=1
s1.stu_name="홍길동"
s1.kor=99
s1.eng=99
s1.math=87
s1.total=s1.kor+s1.eng+s1.math
s1.avg = float("{:.2f}".format(s1.total/3))
s1.rank = 1

print(f"1번학생: {s1.stuNo},{s1.stu_name},{s1.kor},{s1.eng},{s1.math},{s1.total},{s1.avg},{s1.rank}")

class Student:
    
    def __init__(self,stuNo=0,stu_name="",kor=0,eng=0,math=0):
        self.stuNo=stuNo
        self.stu_name = stu_name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float("{:.2f}".format(s1.total/3))
        self.rank = 0

s2 = Student(2,"유관순",98,93,87)
print(f"2번학생: {s2.stuNo},{s2.stu_name},{s2.kor},{s2.eng},{s2.math},{s2.total},{s2.avg},{s2.rank}")

s3 = Student(3,'이순신',88,76,30,194,64.67,6)
print(f"3번학생: {s3.stuNo},{s3.stu_name},{s3.kor},{s3.eng},{s3.math},{s3.total},{s3.avg},{s3.rank}")

stu_list=[s1,s2,s3]