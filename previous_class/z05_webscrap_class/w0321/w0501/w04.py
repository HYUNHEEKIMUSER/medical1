import oracledb

while True:
    
    id = input("아이디 입력하세요 (-1. 종료)")
    if id=='-1':
        break
    
    # id 가지고 검색을 먼저 한 후 데이터를 입력하도록 해야 함.
    # id가 존재하면 id 다시 입력 id가 존재하지 않으면 패스워드 입력 받음

    conn = oracledb.connect(user = "ora_user", password="1111", dsn="localhost:1521/xe")
    cursor = conn.cursor()
    sql == f"select * from member where id ='{id}'"
    cursor.execute(sql)
    data = cursor.fetchall()
    # id가 존재하는 지 
    if len(data) == 1:
        print("id 다시 입력하기")
        print()
        continue
    # id가 존재하지 않으면 계속 입력
    pw = input("패스워드 입력하세요 >> ")
    name = input("이름을 입력하세요 >> ")
    gender = input("성별을 입력하세요 >> ")

    # db연결, 해제
    conn = oracledb.connect(user = "ora_user", password="1111", dsn="localhost:1521/xe")
    cursor = conn.cursor()
    sql = f"insert into member values(member_seq.nextval,'{id}','{pw}','{name}','{gender}',sysdate)"
    cursor.execute(sql)
    cursor.execute('commit')
    print("입력이 완료되었습니다.")
    print()

    cursor.close()
    conn.close()