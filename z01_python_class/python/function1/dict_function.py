# 함수선언 / 한개짜리 변수는 return이 필요하고 리스트는 return이 필요없음
# 리스트와 딕셔너리는 같다
# 리스트[1] 딕셔너리["stuNo"]
def stu_update(student): #지역변수
    student["stuNo"]=2
    student["name"] ="유관순"
    student["total"] = student["kor"]+student["eng"]+student["math"] #지역변수
    student["avg"] = student["total"]/3


# 프로그램 구성
student = {'stuNo': 1, 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33} #2개 이상의 데이터변수


# 함수호출
stu_update(student) # 전역변수

print("학생1: ",student) # 
