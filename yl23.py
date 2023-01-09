import random

suits = ["ärtu", "poti", "risti", "ruutu"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "poiss", "emand", "kuningas", "äss"]
used_cards = []

for i in range(11):

    next_suit = random.choice(suits)
    next_rank = random.choice(ranks)

    while (next_suit + next_rank) in used_cards:
        print(next_rank + next_suit, "on märgitud")
        next_suit = random.choice(suits)
        next_rank = random.choice(ranks)

used_cards.append(next_suit + next_rank)

print(next_suit, next_rank)

print(used_cards)