product = ['새우깡','90g',1200,3]
for i in product:
    print('상품 : {}, 무게 : {}, 가격: {}, 유통기한 : {}'
          .format(product[0],product[1],product[2],product[3]))
    print('상품 : {}, 무게 : {}, 가격: {}, 유통기한 : {}'.format(*product))
    
a_lists = []
for i in range(3):
    a_list =[]
    for j in range(3):
        a_list.append((3*i)+j+1)
    a_lists.append(a_list)
    
print(a_lists)
# -----------------------------------------------
list = []
for i in range (9):
    list.append(i+1)
print(list)
# ==
list2= [n+1 for n in range(9)]
print(list2)
# -----------------------------------------------
list3=[[0]*3 for n in range(3)]
print(list3)

numList = [num*num for num in range(1,6)]
print(numList)

students = [[1,'홍길동',100,99,87,286,95.33,2],
            [2,'유관순',98,93,87,278,92.67,3],
            [3,'이순신',88,76,30,194,64.67,5],
            [4,'김구',100,100,100,300,100.00,1],
            [5,'강감찬',98,85,44,227,75.67,4]]
student = "1,'홍길동',100,99,87,286,95.33,2" 
s_list = student.split()
print(s_list)