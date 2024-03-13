# 함수선언
def stu_update(stuNo, name, kor, eng, math): #지역변수
    name ="유관순"
    stuNo=2
    total = kor+eng+math #지역변수
    avg = total/3
    return total, avg, name, stuNo  # 호출 시 순서 맞추기

# 프로그램 구성
stuNo=1
name ="홍길동"
kor = 100
eng = 100
math = 100
total = 0
avg = 0

# 함수호출
total, avg, name,stuNo = stu_update(stuNo, name, kor, eng, math) # 전역변수

print("학생1: ",stuNo, name, eng, math, total, avg) # 


