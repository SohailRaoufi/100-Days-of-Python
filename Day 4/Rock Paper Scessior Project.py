import random
print("Welcome to rock paper ans scissors game!!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock , paper , scissors]

user_choice = int(input("What Do you Choose? Type 0 -> Rock , 1 -> Paper , 2 -> Scissors.\n"))

computer_choice = random.randint(0 , 2)

if user_choice == computer_choice:
    print(f'Both Chooses\n {game_image[user_choice]}')
    print('Draw')
elif user_choice == 0 and computer_choice == 1:
    print(game_image[user_choice])
    print(f'Computer Choose\n {game_image[computer_choice]} \n You Lose')
elif user_choice == 0 and computer_choice == 2:
    print(game_image[user_choice])
    print(f'Computer Choose\n {game_image[computer_choice]} \n You Win')
elif user_choice == 1 and computer_choice == 0:
    print(game_image[user_choice])
    print(f'Computer Choose\n {game_image[computer_choice]} \n You Win')
elif user_choice == 2 and computer_choice == 0:
    print(game_image[user_choice])
    print(f'Computer Choose\n {game_image[computer_choice]} \n You Lose')
elif user_choice == 2 and computer_choice == 1:
    print(game_image[user_choice])
    print(f'Computer Choose\n {game_image[computer_choice]} \n You Win')
else:
    print("Choose Correct Option!!!")
