#Ask for user input 
# Save data into dictionary{name: price}
# Check if new bids need to be added 
# Compare bids in dictionary 
def find_highest_bid(bidding_dict):
    winner = ""
    highest_bid = 0
    max(bidding_dict)
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
        




bids = {}
continue_bidding = True
while continue_bidding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? 'yes' 'no'. \n").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bid(bids)
    elif should_continue == 'yes':
        print("\n* 20")




