import oracledb

# DB connect 연결
conn = oracledb.connect(user="ora_user", password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

# sql 실행
# employees 테이블에서 사번, 이름, 월급, 실제월급(월급+(월급*커미션)), 월급*1410 원화로 환산해서
# 원화표시 천 단위 표시로 해서 출력
# sql = "select employee_id, emp_name, salary, nvl(salary+(salary*commission_pct),0), \
# salary*1410 from employees"
# cursor.execute(sql)
# data = cursor.fetchall()
# print("[데이터 출력]")
# for d in data[:5]:
#     print(d[0],end='\t')
#     print(d[1],end='\t')
#     print(d[2],end='\t')
#     print(d[3],end='\t')
#     print("원화: ₩{}".format(d[-1],","),end='\t')
  
# sql= "select employee_id, emp_name, salary, salary+(salary*nvl(commission_pct,0)), \
#     to_char(salary*1410,'L999,999,999')as korean from employees"
# cursor.execute(sql)
# data = cursor.fetchall()
# for d in data[:5]:
#     print(d)


    
# 부서별 평균월급 최대월급 최소월급 출력
sql = "select round(avg(salary),2), max(salary), min(salary) from employees group by department_id"
cursor.execute(sql)
data = cursor.fetchall()
for i, d in enumerate(data[:12]):
    print("{}번째 부서별 평균: {}".format(i+1,d[0]), sep='\t')
    print("{}번째 부서별 최대: {}".format(i+1,d[1]), sep='\t')
    print("{}번째 부서별 최소: {}".format(i+1,d[2]), sep='\t')

sql = "select department_id, round(avg(salary),2), max(salary), min(salary)\
from employees where department_id is not null group by department_id order by department_id"
cursor.execute(sql)
data = cursor.fetchall()
for d in data[:5]:
     print(d)
