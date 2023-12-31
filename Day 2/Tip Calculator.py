#Tip Calculator
"""
Requirements:
    1: Take an amount of money as input form user
    2: ask for tip in percentage (10 , 12 ,15)
    3: as how many people are they dividing the bill with.
    4: output the amount required for each person to pay
"""
print("Welcome to the tip calculator.")

#input process
amount = float(input("What was the total bill? $"))
per = int(input("What percentage tip would you like to give? 10 , 12 or 15? "))
people = int(input("How many people to split the bill? "))

#result process

tip = (amount * per) / 100

total_amount = tip + amount
result = total_amount / people

#output
print(f'Each Person should pay: ${result:.2f}')