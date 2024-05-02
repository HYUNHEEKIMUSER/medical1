import oracledb

conn = oracledb.connect(user = 'ora_user',password='1111', dsn ='localhost:1521/xe')
cursor = conn.cursor()

while True:
    search = input("찾고자하는 이름을 입력하세요 (취소는 1)>>")
    # 홍길동 -> 홍 이름이 다 검색되도록 sql 구문
    if search == '1':
        break
    sql = f"select no, name from stu_score where name like '%{search}%'"
    cursor.execute(sql)
    data = cursor.fetchall() 
    for d in data:
            print(d)
    print("데이터갯수: ",len(data))
conn.close()

