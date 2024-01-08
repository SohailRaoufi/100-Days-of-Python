from art import logo , vs
from game_data import data
import random

print(logo)
Score = 0
Times = 0
comp_a = {}
comp_b = {}

def pick_data(data , Times):
    global comp_a
    global comp_b
    if comp_a == {} and comp_b == {}:
        comp_a = random.choice(data)

        comp_b = random.choice(data)
        if comp_a == comp_b:
            comp_b = random.choice(data)
    else:
        comp_a_follower = comp_a['follower_count']
        comp_b_follower = comp_b['follower_count']
        if comp_a_follower > comp_b_follower:
            if Times >= 2:
                comp_a = random.choice(data)
                comp_b = random.choice(data)
            else:
                comp_b = comp_a
                comp_a = random.choice(data)
        else:
            if Times >= 2:
                comp_a = random.choice(data)
                comp_b = random.choice(data)
            else:
                comp_a = comp_b
                comp_b = random.choice(data)


def show_data(comp_a , comp_b):
    print(f"Compare A: Name: {comp_a['name']} , description: {comp_a['description']} , country: {comp_a['country']}")
    print(vs)
    print(f"Compare B: Name: {comp_b['name']} , description: {comp_b['description']} , country: {comp_b['country']}")





while True:
    pick_data(data, Times)
    show_data(comp_a, comp_b)
    if Times >= 2:
        Times = 0
    follower_a = comp_a['follower_count']
    follower_b = comp_b['follower_count']
    print(follower_a , follower_b)
    user = input("A or B: ").lower()
    if user == 'a':
        if follower_a > follower_b:
            Score += 1
            Times += 1
            print(f"You are Right , Score = {Score}")
        else:
            print(f"You Lose!\nScore = {Score}")
            break
    elif user == 'b':
        if follower_b > follower_a:
            Score += 1
            Times += 1
            print(f"You are Right , Score = {Score}")
        else:
            print(f"You Lose!\nScore = {Score}")
            break



