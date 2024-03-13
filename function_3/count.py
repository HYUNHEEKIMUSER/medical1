import random

# 랜덤으로 숫자 1개 생성
ran_num = random.randint(1,100)
# 입력한 숫자보다 크면 작은 수를 입력하세요
in_num = 0
cnt = 1
save = []
while True:
    print("[랜덤숫자 맞추기게임]")
    in_num = int(input(f"{cnt}번쨰 도전. 1~100까지의 숫자를 입력하세요 >>"))
    if ran_num > in_num:
        print("입력한 숫자보다 큰 수를 입력하세요")
        save.append(in_num)
    elif ran_num < in_num:
        print("입력한 숫자보다 작은 수를 입력하세요")
        save.append(in_num)
    else:
        print("정답입니다")
        break
    cnt +=1
# 입력한 숫자보다 작으면 큰 수를 입력하세요 하고 멘트가 나오게 하세요
# 정답을 맞추면 
# 총 입력한 횟수 : 7회
    if cnt == 7:
        print(f"{cnt}번째 도전이 끝났습니다.")
        break
print(f"현재까지 입력한 숫자는 {save}입니다.")


# 현재까지 입력한 숫자 : 1,5,7,6,8,4,50

# 현재까지 입력했던 숫자를 모두 출력


