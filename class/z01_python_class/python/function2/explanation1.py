# 함수를 1,2,3,4,5,6,7,8,9,10
# 더하기 결과값을 출력
# 가변매개변수
# 딕셔너리는 가변매개변수 **
def para_func(*num):
    sum =0
    for n in num:
        sum+=n
    print("합계: ",sum)
        
para_func(1,2)
para_func(1,2,3,4)   




