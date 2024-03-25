import stu_file

# stu.txt 파일열기호출
students=stu_file.stu_open()

s_title = ["","국어","영어","수학"]

# 학생성적화면 함수
def stu_main_print():
    print("-"*40)
    print("\t[학생성적프로그램]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체출력")
    print("3. 학생검색")
    print("4. 학생수정")
    print("5. 등수처리")
    print("6. 학생삭제")
    print("7. 학생성적 파일저장")
    print("0. 프로그램 종료")
    print("-"*40)
    if not choice.isdigit():
        print("숫자만 입력 가능합니다.")
        choice = int(choice)
        return choice
    # 학생성적 입력 
def stu_insert(cnt):
    while True:
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요 (0. 취소)")
        if name == 0:
            print("학생성적 입력 취소")
            break
        student={}
        student["stuNo"] = cnt
        student["name"] = name
        kor = int(input("국어점수를 입력하세요 >> "))
        students["kor"]=kor
        eng = int(input("영어점수를 입력하세요 >> "))
        students["eng"]=eng
        math = int(input("수학점수를 입력하세요 >> "))
        students["math"] = math
        total = kor+eng+math
        student["total"] = total
        avg = total/3
        student['avg']=float("{:.2f}".format(avg))
        students.append(student)
        cnt +=1
        print("입력데이터: ",student)
        print(students)
    
def stu_top_print():
    print('\t[ 학생성적출력 ]')
    print('-'*50)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*50)

def stu_grade_print(stu_list):
    stu_top_print()
    for s_dic in stu_list:
        for s_key in s_dic:
            print(s_dic[s_key], end= '\t')
        print()
    print('-'*50)
    print()

def stu_search():
    search_student=[]
    print("학생성적 검색")
    search = input("찾고자 하는 학생의 이름을 입력하세요 >> ")    
    search_cnt = 0
    for s in students:
        if s['name']==search:
            break
        search_cnt +=1
        
    if len(students) == search_cnt:
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요 >> ")
    else: 
        print(f"{search}학생을 찾았습니다. 성적을 출력합니다.")
        search_students.append(students[search_cnt])
        stu_grade_print(search_students)
        
def stu_subject_update(s_input,chk,s_1):
    print(f"[ {s_title[s_input]} 수정 ]") 
    print(f"현재 {s_title[s_input]}점수: {students[chk][s_1]}")
    print('-'*20)
    score = int(input(f"수정할 {s_title[s_input]}점수를 입력하세요"))   
    students[chk][s_1]=score
    students[chk]['total']=students[chk]["kor"] + students[chk]["eng"]+students[chk]["math"]
    print(f"{s_title[s_input]}점수: {students[chk][s_1]}점으로 수정이 완료되었습니다.")

def stu_update():
    while True:
        search = input("찾고자 하는 학생을 입력하세요 (0.취소)")
        chk= 0
        if search ==0: break
        for s_dic in students:
            if s_dic["name"] == search:
                break
            chk +=1
        print("찾고자 하는 학생의 위치: ",chk)
        if chk == len(students):
            print(f"{search}학생은 없습니다 다시 입력하세요")
        else:
            print(f"{search}학생을 찾았습니다.")
            while True:
                print("[ 수정할 과목 선택 ]")
                print("-"*30)
                print("1.국어\t2.영어\t3.수학")
                s_input=int(input("수정하려는 과목을 선택하세요 >> "))
                if s_input == 1:
                    s_1 = "kor"
                    stu_subject_update(s_input,chk,s_1)
                elif s_input ==2:
                    s_2 = "eng"
                    stu_subject_update(s_input,chk,s_2)
                elif s_input ==2:
                    s_3 = "math"
                    stu_subject_update(s_input,chk,s_3) 
                else:
                    print("과목 수정을 취소합니다.")
                    break
# 등수처리 함수
def stu_rank():
    for s_dic in students:
        rank_cnt =1
        for i_dic in s_dic:
            if s_dic["total"] < i_dic["total"]:
                rank_cnt +=1
        s_dic["rank"]=rank_cnt
    print("등수처리가 완료되었습니다.")
    print(students)

def stu_delete():
    while True:
        search = input("삭제하고자 하는 학생의 이름을 입력하세요 >> ")
        chk = 0
        if search == 0: break
        for s_dic in students:
            if s_dic["name"] == search: break
            chk +=1
            
        print("찾고자 하는 학생의 위치 : ",chk)
        if chk >= len(students):
            print("찾고자 하는 학생이 없습니다.") 
        else:
            print(f"{search}학생을 찾았습니다.")   
            s_input= input("{}학생 성적을 삭제하시겠습니까? (1. 실행, 0. 취소)")
            if s_input !=1:
                print("삭제를 취소합니다")
                break
            else:
                del students[chk]
                print(f"{search}학생의 성적이 삭제되었습니다.")
                print(students)
                
cnt = len(students)+1

while True:
    choice = stu_main_print()
    if choice == 1:
        stu_insert(cnt)
        stu_file.stu_save(students)
        
    elif choice == 2:
        stu_grade_print(students)
    elif choice ==3:
        stu_search()
    elif choice ==4:
        stu_update()
        stu_file.stu_save(students)
    elif choice ==5:
        stu_rank()
        stu_file.stu_save(students)
    elif choice == 6:
        stu_delete()
        stu_file.stu_save(students)
    elif choice == 7:
        stu_file.stu_save(students)
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        print("선택된 서비스가 없습니다.")