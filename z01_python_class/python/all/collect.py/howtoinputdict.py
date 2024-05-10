import operator
fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']
counter ={}
# 딕셔너리 넣는 법
for f in fruit:
    if f not in counter:
        counter[f]=0
    counter [f] +=1
print(counter)

a = [3,5,7,4,12,6]
print(sorted(a))
# 순서 배열
print(dict(sorted(counter.items(),key=operator.itemgetter(0)))) #key
print(dict(sorted(counter.items(),key=operator.itemgetter(1))))  # value

print(sorted(counter.items(),key=operator.itemgetter(0)))
print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))
print(sorted(counter.items(),key=operator.itemgetter(1)))
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))