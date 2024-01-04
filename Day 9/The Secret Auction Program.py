auction_player = {}
ask_user = ''
while ask_user != 'no':
    user_name = input("Enter Player Name: ")
    user_bid = int(input(("Enter The amount: $")))
    auction_player[user_name] = user_bid
    print("write yes if you want to add another player otherwise no")
    ask = input()
    if ask == 'no':
        break


high_bid = 0
winner = ''

for player in auction_player:
    bid = auction_player[player]
    if bid > high_bid:
        high_bid = bid
        winner = player

print(f'The Winner is {winner} with bidding amount of {high_bid}.')

    