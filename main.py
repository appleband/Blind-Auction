from replit import clear
from art import logo

print(logo)

bidders = {}
auction = True
while auction:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n"))

  bidders[name] = bid
  other_bidders = input("Are there other bidders? Enter 'Yes' or 'No'\n")
  if other_bidders == 'Yes':
    clear()
  else:
    auction = False

highest_bid = 0
highest_bidder = ''
for person in bidders:
  a_bid = bidders[person]
  if a_bid > highest_bid:
    highest_bid = a_bid
    highest_bidder = person
print(f"The highest bidder is {highest_bidder} with {highest_bid}")

#HINT: You can call clear() to clear the output in the console.
