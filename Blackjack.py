import random
a = ["Spades","Hearts","Diamonds","Clubs"]
d = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
n = m =0
while (n<21 and m<21):
    print("Player 1: \n")
    suite,no = random.choice(list(d.items()))
    print("Your card is " + str(no) + " of " + random.choice(a) + "\n")
    n += no
    if n>21:
        print("You lose, Player 2 wins")
        break
    if n==21:
        print("Player 1 wins")
    print("Player 2: \n")
    suite,no = random.choice(list(d.items()))
    print("Your card is " + str(no) + " of " + random.choice(a) + "\n")
    m += no
    if m>21:
        print("You lose, Player 1 wins")
        break
    if m==21:
        print("Player 2 wins")
