foods ={'떡볶이':'오뎅','짜장면':'단무지','라면':'김치',
        '피자':'피클','맥주':'땅콩','삼겹살':'상추'}

print(foods.keys())
for key in foods:
    print(key, end = ' ')    
print(foods.values())
for key in foods:
    print(foods[key], end = '\t')
for key in foods:
    print(f'{key}:{foods[key]}')
    
import operator
fruits = {'peach':'복숭아','orange':'오렌지','apple':'사과',"pear":"배",
          'grapes':'포도','mango':'망고','kiwi':'키위'}

print(fruits.keys())
print(fruits.values())
print(fruits.items())

sorted(fruits.items(),key=operator.itemgetter(0),reverse=True)
print(fruits)