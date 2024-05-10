print("문자열")
print(5)
print(123*111)
print("%d %f %s"%(10,12.1,'answer'))
print("%0.2f"%(22.355656))
print("문자열을 쓰고 {}".format(1))
print("{0:d}".format(123))
print("{0}".format(123))
print("{}".format(123))

print("{0:f}".format(123.456458))
print("{0}".format(1230.12546))
print("{}".format(123.45687987))
print("{0:.2f}".format(1236.156))
print("{0:s}".format('문자'))
print("{0}".format('answer'))
print("{}".format('answer'))

print("{0},{2},{1}".format('빨','주','노'))
num = 10
pi = 3.14
result = True
str1 = "문장입니다"
ch = "A"
print(num)
print(result)
s1 = '1+1=2'
print(s1)
s2 = '{}+{}={}'.format(1,1,2)
print(s2)

s2 = '{}'.format(1+1)
print(s2)

a = 1
a = a + 1
a += 1
a -= 1
a *= 1
a /= 1
a, b = 10,20
a = 10
b = 10

print(a==b)
print(a != b)
print(a >= b)
a,b,c = 100,200,150
result = (a>c) and (b<c)
print(result)
print( not a>b)

temp = 0
for i in range(1,10):
    for j in range(1,10):
        if j==5:
            temp =1
            break
        print(f"{i}*{j}={i*j}")
    if temp == 1: break