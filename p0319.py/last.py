def stu_revise():
    search = input("찾는 학생의 이름을 입력하세요>> (0.취소)")
    if search == 0:
        break
    cnt = 0
    count = 0
    for stu in students:
        if search in stu:
            cnt = 1
            break
        print("찾고자 하는 학생의 위치: ",cnt)
        count+=1
        
    if cnt ==len(students):
        print("찾는 학생의 정보가 없습니다.")
    else:
        print(f"{search} 학생의 정보를 찾았습니다.")
        num = int(input("1. 국어 2. 영어 3. 수학"))
        if num == 1:
            print("국어성적 수정을 선택하셨습니다.")
            print('-'*50)
            print(f'{search}님의 국어성적은 {students[count][2]}점 입니다.')
            re_kor = int(input("국어 성적값 입력"))
            students[count][2] = re_kor
            print(f"{search}님의 수정된 국어성적: {re_kor}점")
        elif num ==2:
            print("영어성적 수정을 선택하셨습니다.")
            print('-'*50)
            print(f"{search}님의 영어성적은 {students[count][3]}점 입니다.")
            re_eng = int(input("영어 성적값 입력"))
            students[count][3] = re_eng
            print(f"{search}님의 수정된 영어성적: {re_eng}점")
        elif num == 3:
            print("수학성적 수정을 선택하셨습니다.")
            print('-'*50)
            print(f"{search}님의 수학성적은 {students[count][4]}점 입니다.")
            re_math = int(input("수학 성적값 입력"))
            students[count][4] =re_math
            print(f"{search}님의 수정된 수학성적:{re_math}점")
        else :
            print("잘못입력하셨습니다. 다시 입력하세요")
    students[count][5]= students[count][2]+students[count][3]+students[count][4]
    students[count][6]="{:.2f}".format(students[count][5]/3)
    
    # 1. 이름으로 학생을 검색
    # 2. 찾았으면 과목 선택
    # 3. 과목리스트 출력
    # 4. 국어선택
    # 5. 국어점수 출력 후 국어점수 입력
    # 6. 국어점수 변경 후 이전화면 이동
    # 7. 못 찾았으면 다시 이전화면으로 나옴.
                    