#Day 3 Final Project
print("Welcome to Tresure Island Your Mission is to find the treasure.")
select_way = input("You have to chosse a way ? Right or Left ").lower()

if select_way == 'left':
    print("You Have Reached to an island!")
    choose = input("You want to wait for boat or you want to swim? Wait or Swim ").lower()
    if choose == 'wait':
        print("You have crossed the island with no harm!")
        door = input("Now Choose a door based on color? Red , Blue or Yellow ").lower()
        if door == 'yellow':
            print("You Found the treasure!!!!!")
        elif door == 'red':
            print("You Pick the wrong door, Fire will burn you.")
        elif door == 'blue':
            print("You Pick the wrong door, Animals are waiting.")
    elif choose == 'swim':
        print("Shark eats you and you lost!!!")
elif select_way == 'right':
    print("you fall , Dead End!!!!")