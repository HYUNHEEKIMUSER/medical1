words= [{},{"airplane":"비행기","apple":"사과","bakery":"빵집","banana":"바나나","bank":"은행",
          "bean":"콩","bicycle":"자전거","boat":"보트","bowl":"그릇","bus":"버스"},{"run" : "달리다","walk" : "걷다","sit" : "앉다","stand" : "서다","sleep" : "자다","read" : "읽다",
         "look" : "보다","do" : "하다","feel" : "느끼다","go" : "가다"},{ "accumulated":"누적된",
    "additional":"추가적인",
    "adequate":"적당한",
    "administrative":"관리의",
    "affordable":"알맞은",
    "alternative":"대체 가능한",
    "annual":"해마다의",
    "different":"다른",
    "local":"지역의",
    "social":"사회의"}]

w_noun = {"airplane":"비행기","apple":"사과","bakery":"빵집","banana":"바나나","bank":"은행",
          "bean":"콩","bicycle":"자전거","boat":"보트","bowl":"그릇","bus":"버스"}
w_verb ={"run" : "달리다","walk" : "걷다","sit" : "앉다","stand" : "서다","sleep" : "자다","read" : "읽다",
         "look" : "보다","do" : "하다","feel" : "느끼다","go" : "가다"}
w_ad= { "accumulated":"누적된",
    "additional":"추가적인",
    "adequate":"적당한",
    "administrative":"관리의",
    "affordable":"알맞은",
    "alternative":"대체 가능한",
    "annual":"해마다의",
    "different":"다른",
    "local":"지역의",
    "social":"사회의"}

w_title = ["","명사","동사","형용사"]

while True:
    print("[영단어 맞추기 프로그램]")
    print("-"*40)
    print("1. 명사")
    print("2. 동사")
    print("3. 형용사")
    print("0. 종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요>>"))
    print("-"*40)
    correct =0
    wrong = 0
    if choice == 1:
        print("{}를 선택했습니다".format(w_title[choice]))
        chk = input("퀴즈 준비가 되었나요? 1번 실행 0번 취소")
        if chk == "1":
            for key in words[choice]:
                answer = input("{}단어의 뜻은?".format(key))
                if answer==words[choice][key]:
                    print("정답입니다.")
                    correct +=1
                else :
                    print("오답입니다. 정답 : {}".format(w_noun[key]))
                    wrong +=1
            print("[명사 맞추기 퀴즈가 끝났습니다]")
            print(f"맞춘 갯수:{correct}개, 틀린 갯수: {wrong}개")
            
        else :
            print("퀴즈를 실패하셨습니다")
    elif choice == 2:
        print("{}를 선택했습니다".format(w_title[choice]))
        chk = input("퀴즈 준비가 되었나요? 1번 실행 0번 취소")
        if chk == "1":
            for key in w_verb:
                answer = input("{}단어의 뜻은?".format(key))
                if answer==words[choice][key]:
                    print("정답입니다.")
                    correct +=1
                else :
                    print("오답입니다. 정답 : {}".format(w_noun[key]))
                    wrong +=1
            print("[동사 맞추기 퀴즈가 끝났습니다]")
            print(f"맞춘 갯수:{correct}, 틀린 갯수: {wrong}")
    elif choice == 3:
        print("{}를 선택했습니다".format(w_title[choice]))
        chk = input("퀴즈 준비가 되었나요? 1번 실행 0번 취소")
        if chk == "1":
            for key in w_ad:
                answer = input("{}단어의 뜻은?".format(key)) 
                if answer==words[choice][key]:
                    print("정답입니다.")
                    correct +=1
                else :
                    print("오답입니다.")
                    wrong +=1
            print("[형용사 맞추기 퀴즈가 끝났습니다]")
            print(f"맞춘 갯수:{correct}, 틀린 갯수: {wrong}")

    else:
        print("프로그램 종료하겠습니다")
        break