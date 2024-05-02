import oracledb
# sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성
sql = '''select no, name,total, avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
else 'F'
end as grade
from stu_score_cdate '''
# sql = "select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile \
#         from board a,member b \
#         where a.id = b.id "
# stu_score avg 90점 이상 A, 80이상 B,C,D, 60점 미만 F
# 학번,이름,합계,평균,학점 출력하시오.
# board테이블 id포함 모든 컬럼, member테이블의 name컬럼을 가져와 출력하시오.
# board테이블 id, member테이블 name
# sql = "select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile \
#         from board a,member b \
#         where a.id = b.id"
# cursor.execute(sql)      # cursor에 select한 결과값을 저장(결과값 : list)
# data = cursor.fetchall() # fetchall():모든 데이터 가져옴. fetchone() : 1개의 데이터 가져옴.
# print("[ 모든 데이터 출력 ]")
# # print(data)
# for d in data[:5]:
#     print(d)
#     print("평균: ",float(d[3]))
#     print("-"*20)
# print("-")
# print("타입 : ",type(data))

# salary 평균 출력
sql = "select round(avg(salary),2) from employees"
cursor.execute(sql)
data= cursor.fetchone()  #데이터 한 개만 넘겨 오는 것
print("salary 평균 : ",data)
print(data[0])
conn.close()