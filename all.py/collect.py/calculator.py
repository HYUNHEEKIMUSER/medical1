n1 = int(input("숫자"))
cal = input("수식 입력 (+,-,*,/) ->")
n2 = int(input("숫자?"))
again = input("수식 입력 (+,-,*,/) ->")

if cal == '+':
    print(n1+n2)
elif cal == '-':
    print(n1-n2)
elif cal == '*' :
    print(n1*n2)
elif cal == '/' :
    print(n1/n2)
elif cal != '+' and cal != '-' and cal != '/' and cal != '*':
    print(again)