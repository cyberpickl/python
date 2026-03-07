from art import logo
print(logo)
print("\n"*2)

print("####################################")
print("Welcome to the Blind Auction Program!")
print("####################################")

print("\n"*2)

bidders={}
name=input("What is your name: ")
amount=bidders[name]=int(input("What is your bid: "))
more=input("Are there are other bidders? (Yes/No): ")
print("\n"*100)

while more== "y":
    name=input("What is your name: ")
    amount=bidders[name]=int(input("What is your bid: "))
    more=input("Are there are other bidders? (Yes/No): ")
    print("\n"*100)


highest_bid = 0
for name in bidders:
    if bidders[name]>highest_bid:
        highest_bid = bidders[name]
        winner = name 

print(f"The winner is {winner} with a bid of amount:${highest_bid}")






