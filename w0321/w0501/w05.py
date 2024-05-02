import oracledb
conn = oracledb.connect(user = "ora_user", password="1111", dsn = "localhost:1521/xe")
cursor = conn.cursor()
# ddl 명령어는 commit이 없음, create alter, drop 
# dml 명령어: insert, update, delete, select
sql = "create table mem(\
id varchar2(30) primary key,\
pw number,\
name varchar2(30),\
mdate date\
)"
cursor.execute(sql)

print("테이블 생성완료")




cursor.close()
conn.close()