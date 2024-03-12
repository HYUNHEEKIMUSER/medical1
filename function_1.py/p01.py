students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]
cnt = len(students)+1
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        continue # 반복문 계속실행
    choice = int(choice)
    
    # 학생성적입력
    if choice == 1:
        print("학생성적입력을 선택하셨습니다")
        name = input("검색하고 싶은 이름을 작성하세요 (0번은 취소)>> ")
        if name == 0:
            print("취소하겠습니다")
            break
        else :
            print(f"{name}이 검색되였습니다.")
            print(f"[{name}님의 학생성적]")
            new_student = {}
            new_student["stuNo"] = 's'+'{:03d}'.format(cnt)
            new_student["name"] = name
            new_kor = int(input("국어 성적을 입력하세요"))
            new_student["kor"] = new_kor
            new_eng = int(input("영어 성적을 입력하세요"))
            new_student["eng"]=new_eng
            new_math = int(input("수학 성적을 입력하세요"))
            new_student["math"]=new_math
            new_total = new_kor+new_eng+new_math
            new_student["total"] = new_total
            new_avg = new_total/3
            new_student["avg"]=new_avg
            students.append(new_student)
            cnt +=1
            print(new_student)
    # 학생성적 전체출력
    if choice == 2:
        count = int(input("학생성적 전체 출력을 하시겠습니까? (0번은 취소, 1번 실행)"))
        if count == 0:
            break
        else:
            print("학생성적 전체를 출력하셨습니다")
            print('-'*40)
            print("학번\t이름\t국어\t영어\t수학\t총합\t평균")
            print('-'*40)
            for s_dic in students:
                for s_key in s_dic:
                    print(s_dic[s_key], end = '\t')
            print('-'*40)
            print()
    #  학생검색
    if choice ==3 :
        search = int(input("학생을 검색하시겠습니까? (0번은 취소, 1번은 실행)"))
        if search == 0:
            break
        chk = 0
        count = 0
        for s_dic in students:
            if s_dic["name"]== search:
                break
        cnt +=1
        
        if search == 1:
            print(f"{search}학생을 검색하겠습니다.")
            print(f"{search}학생 성적의 검색내역입니다.")
            print('-'*40)
            print("학번\t이름\t국어\t영어\t수학\t총합\t평균")
            print('-'*40)
            for i in students[count]:
                print(i , end = '\t')
            print('-'*40)
            print()
        
    # 학생수정
    if choice == 4:
        title=["","국어","영어","수학"]
        search = int(input("학생을 검색하시겠습니까? (0번은 취소, 1번은 실행)"))
        if search == 0:
            break
        chk = 0
        count = 0
        for s_dic in students:
            if s_dic["name"]==search:
                break
        cnt += 1
        if search ==1:
            print(f"{search}학생의 성적을 수정하겠습니다.")
            subject = input("수정하고 싶은 과목을 선택하세요 1. 국어 2. 영어 3. 수학")
            if subject == 1:
                print(f"{search}학생의 {title[subject]}성적을 수정하겠습니다.")
                print(f"{title[subject]}의 현재 점수: {students[chk]["kor"]}")
                score = int(input("점수를 입력하세요 >> "))
                students[chk]["kor"] =score
                students[chk]["total"] = students[chk]["math"]+students[chk]["eng"]+score
                students[chk]["avg"]=float("{:.2f}".format(students[chk]["total"]/3))
                print(f"{title[subject]}점수가 {score}점으로 수정되었습니다")
            elif subject == 2:
                print(f"{search}학생의 {title[subject]}성적을 수정하겠습니다.")
                print(f"{title[subject]}의 현재 점수: {students[chk]["eng"]}")
                score = int(input("점수를 입력하세요 >> "))
                students[chk]["eng"] =score
                students[chk]["total"] = students[chk]["math"]+students[chk]["kor"]+score
                students[chk]["avg"]=float("{:.2f}".format(students[chk]["total"]/3))
                print(f"{title[subject]}점수가 {score}점으로 수정되었습니다")
            elif subject == 3:
                print(f"{search}학생의 {title[subject]}성적을 수정하겠습니다.")
                print(f"{title[subject]}의 현재 점수: {students[chk]["math"]}")
                score = int(input("점수를 입력하세요 >> "))
                students[chk]["math"] =score
                students[chk]["total"] = students[chk]["eng"]+students[chk]["kor"]+score
                students[chk]["avg"]=float("{:.2f}".format(students[chk]["total"]/3))
                print(f"{title[subject]}점수가 {score}점으로 수정되었습니다")
            else : 
                print("과목 수정을 취소합니다")
                break
            
    # 학생 등수처리
    if choice == 5:
        print('등수 처리를 선택하셨습니다.')
        for i, s_rank in enumerate(students):
            rank_in = 0
            for d_rank in students:
                if s_rank["total"] < d_rank["total"]:
                    rank_in +=1
                s_rank["rank"] = rank_in
                print("등수처리가 완료되었습니다")    
                rank_in +=1
    
    # 학생삭제
    if choice == 6:
        print("학생삭제를 선택하셨습니다")
        search = input("삭제할 학생의 이름을 검색하세요")
        if search == 0:
            break
        chk = 0
        count = 0
        for s_dic in students:
            if s_dic["name"]== search:
                break
        cnt +=1 
        print(f"{search}학생이 검색되었습니다.")
        dele = int(input("정말 삭제하시겠습니까? 0번 취소, 1번 실행"))
        if dele == 0:
            print("취소하겠습니다")
        else :
            del students[chk]
            print("삭제를 완료 하였습니다.")
            print(students)
            break   
    
    if choice == 0:
        print("프로그램을 종료합니다.") 
        break       
                
        