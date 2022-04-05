"""
Урок 1
У нас есть список покупок и мы хотим понять
сколько денег нам с собой брать.
У нас есть бумажные купюры: 500, 100, 50
Есть монеты: 10, 5, 1
Нужно вывести сколько каждого типа нам нужно.
"""

'''
int - только цклые числа
float - дробные числа
'''

# shop_item_str = input('Insert item cost: ')
# shop_item = float(shop_item_str)
# print(type(shop_item_str), type(shop_item))

"""
item_number = 10
total_price = 0
while item_number > 0:
    shop_item = float(input('Insert item cost: '))
    total_price += shop_item
    #total_price += float(input('Insert item cost: '))
    item_number -= 1  #item_number = item_number - 1
"""

item_number = 2
total_price = 0

for i in range(item_number): #range(start, end, step)
    total_price += float(input('Insert item cost: '))

'''
/ - деление (вернет флоат с дробной частью)
// - целчисленное деление (вернет флоат, но только целую часть)

'''

rub_500 = total_price // 500 #сколько целых 500
left_money = total_price % 500 #что осталось после 500

print('500 rub: ' + str(rub_500) + 'left: ' + str(left_money))

rub_20 = left_money // 20 #сколько целых 20
left_money = left_money % 20 #что осталось после 20

print(rub_20, left_money)






