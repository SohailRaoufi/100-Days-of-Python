print("Welcome to the Love Calculator!")
name1 = input("What's your name? \n").lower()
name2 = input("What's their name? \n").lower()

count_true = (name1 + name2).count('t') + (name1 + name2).count('r') + (name1 + name2).count('u') + (name1 + name2).count('e')
count_love = (name1 + name2).count('l') + (name1 + name2).count('o') + (name1 + name2).count('v') + (name1 + name2).count('e')

result = int(f'{count_true}{count_love}')

if result < 10 or result > 90:
    print(f'Your score is {result}% , you go togheter like coke and mentos.')
elif result > 40 and result < 50:
    print(f'Your Score is {result}%, you are alright together.')
else:
    print(f'Your Score is {result}%.')
    
