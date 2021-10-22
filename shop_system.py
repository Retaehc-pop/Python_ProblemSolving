item = {}
while True:
    item_name = input()
    if item_name == 'quit':
        break
    elif item_name in item.keys():
        print('duplicate item')
    else:
        item[item_name] = {}
        item_price = int(input(f'price of {item_name}'))
        item_amount = int(input(f'amount of {item_name}'))
        item[item_name]['price'] = item_price
        item[item_name]['amount'] = item_amount
        item[item_name]['buy'] = 0

while True:
    item_name = input('item = ')
    if item_name.lower() == 'quit':
        break
    elif not item_name in item.keys():
        print("No item Found, re-enter item name")
    else:
        print(f'how many {item_name} do you want?')
        item_amount = int(input('amount = '))
        if 0 < item_amount <= item[item_name]['amount']:
            item[item_name]['amount'] -= item_amount
            item[item_name]['buy'] += item_amount
        else:
            print('amount error, re-enter item name')

reciept = '''
-------
reciept
-------
item\tamount\ttotal
'''
final_price = 0
for i in item.keys():
    if item[i]['buy'] != 0:
        total = f"{i} \t {item[i]['buy']} \t {item[i]['price']*item[i]['buy']}\n"
        final_price += item[i]['price']*item[i]['buy']
        reciept += total
reciept += f"""
-------
total {final_price}
_______
"""
print(reciept)
