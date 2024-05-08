n1 = 10
n2 = 13
# print (n1+n2)

n3 = int(10)
n4 = int(13)
print('{}'.format(int(n3)+int(n4)))
print("{}".format(int(n3)*int(n4)))

n5 = input("숫자")
n6 = input("나머지")
print(int(n5)+int(n6))

print('{}+{}={}'.format(10,10,20))

n7 = int(10)
n8 = int(10)
print('{}'.format(int(n7)+int(n8)))

pi = 3.14195
r = input("반지름")
r = int(r)
n = 2*pi
n1 = n * r
n2 = pi * (r ** 2)

print("원의 넓이: {}".format(pi * (r ** 2)))
print("원의 둘레: {}".format(2*pi*r))

money = 13123400

money5 = money//50000
money1 =(money%50000)//10000
money1000 = (((money%50000)%10000)%5000)//1000
money5000 = ((money%50000)%10000)//5000