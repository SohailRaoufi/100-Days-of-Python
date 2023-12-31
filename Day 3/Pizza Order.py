#pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?(S , M , L) ")
add_pepperoni = input("Do you want pepperoni?[Y/N] ")
extra_chesse = input("Do you want extra chesse?[Y/N] ")

bill_amount = 0

if size == "S":
    if add_pepperoni == 'Y':
        bill_amount += 2
    if extra_chesse == 'Y':
        bill_amount += 1
    bill_amount += 15
elif size == "M":
    if add_pepperoni == 'Y':
        bill_amount += 3
    if extra_chesse == 'Y':
        bill_amount += 1
    bill_amount += 20
elif size == "L":
    if add_pepperoni == 'Y':
        bill_amount += 3
    if extra_chesse == 'Y':
        bill_amount += 1
    bill_amount += 25
else:
    print("Chosse from given Size!!!!")
    

print(f'Your final bill is: ${bill_amount}')


    

    