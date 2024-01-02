import random
from Hangman_art import stages , logo
from Hangman_word_list import word_list


print(logo)

lives = 6
chosen_word = random.choice(word_list)
lst_show = []

for i in range(len(chosen_word)):
    lst_show.append("_")
               

while lives > 0:
    user_guess = input("Guess The Latter!!\n")

    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            lst_show[i] = user_guess
    print(f"{' '.join(lst_show)}")
    
    if user_guess not in lst_show:
        print(f'You guessed {user_guess} which is not in word , You lose a live.')
        lives -= 1
        print(stages[lives])
    
    if '_' not in lst_show:
        print("You Won!!")
        break

else:
    print("You LOSE!!!!")
    
    
    

    

    
