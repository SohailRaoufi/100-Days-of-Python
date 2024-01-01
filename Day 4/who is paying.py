import random
names_str = input("Enter Everbody names seprate by comma:")
name_lst = names_str.split(",")

person = random.randint(0 , len(name_lst) - 1)
print(f'{name_lst[person]} is going to buy the meal today!')