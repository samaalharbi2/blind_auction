## Day 9 - Section 9: Beginner - Dictionaries, Grading Program
# TODO-1: As; the user for input
# TODO-2: Save data inor dictionary {name: price}
#TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import blind_auction_art

print(blind_auction_art.logo)


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


def get_bid():
    while True:
        try:
            price = int(input("What is your bid?: $"))
            return price
        except ValueError:
            print("Please enter a valid number.")


bids = {}
conting_bidding = True

while conting_bidding:
    name = input("What is your name?: ")
    price = get_bid()  # Call the function to get a valid bid
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        conting_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)



