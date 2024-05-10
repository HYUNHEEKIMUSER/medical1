import oracledb
# 포트 프로그램 주소 ip 인터넷에 연결된 모든 디바이스 할당되는 식별번호
import math

conn = oracledb.connect(user="ora_user", password ="1111", dsn = "localhost:1521/xe")
# 오라클 처음 접속할 때 열리는 창 : cursor
cursor = conn.cursor()

# 최초 번호
num = 0
# 예로 10개씩 나눠서 보여주도록 구성
# 가져오는 방법
perCount = 10
startrow = 1
endrow = 10
limit = 0

search = input("찾고자 하는 학생 이름을 입력하세요 >>")
sql = f"select count(*) from(select row_number() over(order by no) rnum, a.* from stu_score a where id like '%{search}%')"
cursor.execute(sql)
all_count = cursor.fetchone()
# 3.1일 때 4번 돌아야 함
limit = math.ceil((all_count[0])/perCount)

while True:
    if num !=0:
        print("1. <이전",end = '\t')
        print("2. 다음> ")
        no= input("원하는 번호를 입력하세요")
        if no == "1":
            if num ==1 :
                num = 1
            else :
                num -= 1
        else : 
            num += 1
            if num > limit:num = limit
        print("현재 번호: ",num)
        # 예로 10개씩 나눠서 보여주도록 구성
        # 가져오는 방법
        startrow = (num-1)*perCount+1 # 1,11,21,31......
        endrow = startrow+perCount-1 #10, 20......
    else:
        num+=1
 
    sql = f"select * from(select row_number() over(order by no) rnum, a.* from stu_score a where id like '%{search}%') where rnum>={startrow} and rnum <={endrow}"
    cursor.execute(sql)
    data = cursor.fetchall()
    print("[학생 검색 데이터]")

    for d in data :
        print(d)
        
    print("-"*30)
    print("검색된 페이지: ",num,"검색된 데이터 수: ",all_count)        
    # 최초 실행 시
    if(num==1):
        num += 1 

    num +=1
    print("증감 번호: ",num)
