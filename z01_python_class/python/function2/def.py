# 안녕하세요 반복횟수 3
# 매개변수 순서, 타입이 중요하다
def str_print(txt, num):
    for _ in range(num):
        print(txt)

txt = input("출력하고 싶은 글자를 입력하세요 >>")
num = int(input("출력하고 싶은 글자 반복횟수를 입력하세요 >> "))
str_print(txt,num)