import random

score = 0
print("your score is:", score)
coin = ["tails", "heads"]
while True:
 flip = random.choice(coin)



 player = input("what side of the coin are u picking? heads or tails?: ")
 if player not in coin:
   print("you have to pick a side")
   continue

 if player == flip:
    print("You got it!!")
    score = score + 300
    print("your score is:", score)
 else:
    print("You lost..")
    score = score - 200
    print("your score is:", score)