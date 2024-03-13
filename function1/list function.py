# 함수선언 / 한개짜리 변수는 return이 필요하고 리스트는 return이 필요없음
def stu_update(student): #지역변수
    student[0]=2
    student[1] ="유관순"
    student[5] = student[2]+student[3]+student[4] #지역변수
    student[6] = student[5]/3


# 프로그램 구성
student = [1,"홍길동",100,100,100,0,0] #2개 이상의 데이터변수


# 함수호출
stu_update(student) # 전역변수

print("학생1: ",student) # 
