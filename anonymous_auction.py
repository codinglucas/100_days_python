new_participant = True
while new_participant:
    name = str(input("Input name: "))
    bid = int(input("Bid: "))
    auction = {}

    auction[name] = bid

    restart = input("New participant? \n").lower()
    print("\n" * 500)
    if restart == "no":
        new_participant = False

highest = max(auction, key=auction.get)
print(f"The winner is {highest} with the bid of ${max(auction.values())}")
