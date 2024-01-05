from art import logo
print(logo)


# addition function
def add(num1, num2):
    return num1 + num2

# Subtraction function


def subtract(num1, num2):
    return num1 - num2

# Multiplication


def multiply(num1, num2):
    return num1 * num2

# divition


def divide(num1, num2):
    return num1 / num2


operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide}

num1 = float(input("Enter The First Number?: "))

for symbol in operations:
    print(symbol)

op_symbol = input("Pick and operation from above: ")
num2 = float(input("Enter The second Number?: "))

func = operations[op_symbol]
res = func(num1, num2)

print(f'{num1} {op_symbol} {num2} = {res}')

ask = ''
while ask != 'n':
    ask_user = input(f"Type Y to do operation with {res} or N to exit: ").lower()
    if ask_user == 'y':
        for symbol in operations:
            print(symbol)

        op_symbol = input("Pick and operation from above: ")
        num3 = float(input("Enter the next number?: "))

        func = operations[op_symbol]
        new_res = func(res, num3)

        print(f'{res} {op_symbol} {num3} = {new_res}')
    elif ask_user == 'n':
        ask = 'n'
