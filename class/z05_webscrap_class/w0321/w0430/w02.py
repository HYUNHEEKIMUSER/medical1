import oracledb


conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # db와 연결되어 지시자 생성


sql = "select no, name, total, avg, case when avg>=90 then 'A'\
when avg >=80 then 'B' when avg >=70 then 'C' else 'F' end as grade from stu_score_cdate"
# sql = "select * from stu_score_cdate"
cursor.execute(sql)  #cursor에 select한 결과값을 저장(결과값: list)
data = cursor.fetchall() # 모든 데이터를 다 가져옴 fetchall/ fetchone() 1개의 데이터를 가져옴
print(data[0])
# 평균을 가지고 학점 출력, 학번 이름 합계 평균 학점
sql ="select * from stu_score_cdate"

if data[0][3] >=90:
    print("학점은 A")
    print("학번: ",data[0][0], "이름: ",data[0][1], "총점: ",data[0][2], "평균: ",data[0][3])
elif data[0][3] >=80:
    print("학점은 B")
    print("학번: ",data[0][0], "이름: ",data[0][1], "총점: ",data[0][2], "평균: ",data[0][3])
elif data[0][3]>=70:
    print("학점은 C")
    print("학번: ",data[0][0], "이름: ",data[0][1], "총점: ",data[0][2], "평균: ",data[0][3])
else : 
    print("F")
    
    
    
    
    
    
# print("[모든 데이터 출력]")
# for d in data[:5]:
#     print(d)
#     print("학번: ",d[0])
#     print("이름: ",d[1])
#     print("국어: ",d[2])
#     print("영어: ",d[3])
#     print("수학: ",d[4])    
#     print("-"*20)
# print("-")
# print("타입: ",type(data))

# # 이름이 두 번째에 a가 있는 학생을 출력하시오 학번으로 순차정렬

# sql = "select * from stu_score where name like '_a%' order by no asc"
    
# # board 정보에서 id, name 포함해서 데이터를 가져와 출력
# sql = "select id, name from board a, member b where a.id=b.id"
# # board 테이블 id, member 테이블 name
# # board 테이블 모든 컬럼, member 테이블의 name 컬럼을 가져와 출력
# sql = "select bno, a.id,name,btitle, bcontent, bdate,bgroup, bstep, bindent, bhit, bfile \
# from board a, member b where a.id=b.id"

# stu_score_cdate에서 avg 90점 이상 A, 80점 이상 B,C,D 60점 미만 F
# 학번 이름 합계 평균 학점 출력

# sql = "select no, name, total, avg, case when avg>=90 then 'A'\
# when avg >=80 then 'B' when avg >=70 then 'C' else 'F' end as grade from stu_score_cdate"
# cursor.execute(sql)  #cursor에 select한 결과값을 저장(결과값: list)
# data = cursor.fetchall() # 모든 데이터를 다 가져옴 fetchall/ fetchone() 1개의 데이터를 가져옴

