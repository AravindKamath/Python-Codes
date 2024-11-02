import random
while True:
    p1=input("p1: enter rock,paper or scissor ").lower()
    p2=random.choice(["rock","paper","scissor"]).lower()
    print("p2 selected ",p2)
    if p1 == "rock" and p2 == "paper":
        print("p2 won ")
    elif p1 == "paper" and p2 == "scissor":
        print("p2 won")
    elif p1 == "scissor" and p2 == "rock":
        print("p2 won")
    elif p1 == p2:
        print("tie ")
    else:
        print("p1 won")