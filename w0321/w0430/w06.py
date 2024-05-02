import oracledb
conn = oracledb.connect(user = 'ora_user',password='1111', dsn ='localhost:1521/xe')
cursor = conn.cursor()

# 평균점수를 입력받아 입력한 평균점수 이상의 학생을 출력하시오
# 반복해서 진행하고 -1을 입력받으면 프로그램 종료
# score = int(input("평균 점수를 입력하세요 >> "))

# while True:
#     if score == -1:
#        break
#     sql = "select name, round(avg,2) from stu_score_cdate"
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     for d in data[:10]:
#         if score > data[d][1]:
#                 print("평균점수: ",d)
                
while True:               
    score = int(input("평균 점수를 입력하세요 (-1은 종료)>> "))
    if score == -1:
        break
    print("1.점수 이상")
    print("2.점수 미만")
    
    num_str = input("점수 이상 또는 이하를 선택하세요 >>")
    if num_str == '1':
        sql = f"select round(avg,1) from stu_score_cdate where avg >={score} order by no"
    else : 
        sql = f"select round(avg,1) from stu_score_cdate where avg <{score} order by no"
    cursor.execute(sql)
    data = cursor.fetchall()               
    for d in data:
        print(d)
        print("검색된 데이터 갯수: ",len(data))
        print()
        conn.close()
print("프로그램 종료")
conn.close()