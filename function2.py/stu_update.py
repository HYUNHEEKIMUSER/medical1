
# 성적성적부분 점수
def s_update(choice,s_title,stu):
    stu = [1,"홍길동",100,100,100,300,100.0]
    s_title = ["","국어","영어","수학"]
    print(f"[{s_title[choice]}성적 수정]")
    print(f"현재 {s_title[choice]} 점수: {stu[choice+1]}")
    print('-'*30)
    stu[choice+1] =int(input("수정할 점수를 입력하세요 >>"))
    print("수정된 점수 : ",stu[choice+1])
    stu[5]=stu[2]+stu[3]+stu[4]
    stu[6]=float("{:.2f}".format(stu[5]/3))
    print(stu)
    print(f"{s_title[choice]} 점수가 수정되었습니다.")
    
# 학생성적수정함수
def stu_update(choice,s_title,stu):
    print("[학생성적수정]")
    print("1. 국어 2. 영어 3. 수학")
    choice = int(input("원하는 번호를 입력하세요 >>"))
        
    if choice == 1:
        s_update(choice,s_title,stu)
            
    elif choice == 2:
        s_update(choice,s_title,stu)
                
    elif choice == 3:
        s_update(choice,s_title,stu)