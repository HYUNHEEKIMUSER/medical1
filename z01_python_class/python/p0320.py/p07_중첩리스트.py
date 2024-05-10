a_list = [1,2,[3,4],5,[6,7,8,9],[10,11]]
aa_list = []
for a in a_list:
    if type(a)==list:
        for i in a:
            aa_list.append(i)
            print(i, end="")
    else:
        print(a)
        aa_list.append(a)
print("-"*50)
print(aa_list)

print(list(range(10)))

[i for i in range(10)]
# ------------------------------------------
def func(n,*val,a=2):   #기본매개변수, 가변매개변수 #키워드매개변수(sep, end..)
    for i in range(n):
        for v in val:
            print(v)
func(5,"안녕")