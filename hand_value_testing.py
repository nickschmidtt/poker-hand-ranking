# Nick Schmidt
# September 18, 2024
# Hand Value Testing

from card_ranking_logic import poker_hand
from card_ranking_logic import card

## Test each possible poker hand variation
# royal flush with one pair
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",8)
c5 = card("clubs",8)
c6 = card("spades",11)
c7 = card("spades",10)

poker1 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker1.hand_value() == (9,[14])

# royal flush
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",3)
c5 = card("clubs",8)
c6 = card("spades",11)
c7 = card("spades",10)

poker2 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker2.hand_value() == (9,[14])

# royal flush with three of a kind
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",10)
c5 = card("clubs",10)
c6 = card("spades",11)
c7 = card("spades",10)

poker3 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker3.hand_value() == (9,[14])

# royal flush full with 7 card flush
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("spades",8)
c5 = card("spades",9)
c6 = card("spades",11)
c7 = card("spades",10)

poker4 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker4.hand_value() == (9,[14])

# royal flush full with 7 card straight
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",9)
c5 = card("clubs",8)
c6 = card("spades",11)
c7 = card("spades",10)

poker5 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker5.hand_value() == (9,[14])

# straight flush
c1 = card("spades",7)
c2 = card("spades",8)
c3 = card("spades",6)
c4 = card("clubs",2)
c5 = card("spades",9)
c6 = card("spades",5)
c7 = card("diamonds",3)

poker6 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker6.hand_value() == (8,[9])

# straight flush with 7 cards
c1 = card("spades",9)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("spades",8)
c5 = card("spades",7)
c6 = card("spades",11)
c7 = card("spades",10)

poker7 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker7.hand_value() == (8,[13])

# straight flush with three of a kind
c1 = card("spades",9)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",12)
c5 = card("clubs",12)
c6 = card("spades",11)
c7 = card("spades",10)

poker8 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker8.hand_value() == (8,[13])

# straight flush with two pairs
c1 = card("spades",9)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",9)
c5 = card("clubs",12)
c6 = card("spades",11)
c7 = card("spades",10)

poker9 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker9.hand_value() == (8,[13])

# straight flush with one pair
c1 = card("spades",9)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",5)
c5 = card("clubs",5)
c6 = card("spades",11)
c7 = card("spades",10)

poker10 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker10.hand_value() == (8,[13])

# four of a kind
c1 = card("spades",9)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",12)
c6 = card("spades",11)
c7 = card("spades",10)

poker11 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker11.hand_value() == (7,[12,11])

# four of a kind with one pair
c1 = card("spades",9)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",12)
c6 = card("hearts",10)
c7 = card("spades",10)

poker12 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker12.hand_value() == (7,[12,10])

# four of a kind with three of a kind
c1 = card("diamonds",10)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",12)
c6 = card("hearts",10)
c7 = card("spades",10)

poker13 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker13.hand_value() == (7,[12,10])

# full house with two three of a kinds
c1 = card("diamonds",11)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",11)
c6 = card("hearts",11)
c7 = card("spades",6)

poker14 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker14.hand_value() == (6,[12,11])

# full house
c1 = card("diamonds",11)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",11)
c6 = card("hearts",5)
c7 = card("spades",7)

poker15 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker15.hand_value() == (6,[12,11])

# full house with three of a kind value lower than two of a kind
c1 = card("diamonds",11)
c2 = card("hearts",4)
c3 = card("clubs",4)
c4 = card("diamonds",4)
c5 = card("spades",11)
c6 = card("hearts",5)
c7 = card("spades",7)

poker16 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker16.hand_value() == (6,[4,11])


# full house with two pairs
c1 = card("diamonds",11)
c2 = card("hearts",4)
c3 = card("clubs",4)
c4 = card("diamonds",4)
c5 = card("spades",11)
c6 = card("hearts",9)
c7 = card("spades",9)

poker17 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker17.hand_value() == (6,[4,11])

# flush
c1 = card("diamonds",11)
c2 = card("hearts",7)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",10)
c6 = card("diamonds",9)
c7 = card("diamonds",2)

poker18 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker18.hand_value() == (5,[11,9,5,4,2])

# flush with pair
c1 = card("diamonds",11)
c2 = card("hearts",7)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",11)
c6 = card("diamonds",9)
c7 = card("diamonds",2)

poker19 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker19.hand_value() == (5,[11,9,5,4,2])

# flush with three of a kind
c1 = card("diamonds",11)
c2 = card("hearts",11)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",11)
c6 = card("diamonds",9)
c7 = card("diamonds",2)

poker20 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker20.hand_value() == (5,[11,9,5,4,2])

# flush with two pairs
c1 = card("diamonds",11)
c2 = card("hearts",11)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",9)
c6 = card("diamonds",9)
c7 = card("diamonds",2)

poker21 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker21.hand_value() == (5,[11,9,5,4,2])

# flush with straight
c1 = card("diamonds",11)
c2 = card("hearts",10)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",9)
c6 = card("diamonds",8)
c7 = card("diamonds",7)

poker22 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker22.hand_value() == (5,[11,8,7,5,4])

# flush with all seven cards
c1 = card("diamonds",11)
c2 = card("diamonds",10)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("diamonds",6)
c6 = card("diamonds",13)
c7 = card("diamonds",7)

poker23 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker23.hand_value() == (5,[13,11,10,7,6])

# straight
c1 = card("diamonds",11)
c2 = card("spades",10)
c3 = card("clubs",5)
c4 = card("hearts",9)
c5 = card("diamonds",6)
c6 = card("clubs",12)
c7 = card("diamonds",8)

poker24 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker24.hand_value() == (4,[12])

# straight with pair
c1 = card("diamonds",4)
c2 = card("spades",4)
c3 = card("clubs",5)
c4 = card("hearts",14)
c5 = card("diamonds",3)
c6 = card("clubs",2)
c7 = card("diamonds",2)

poker25 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker25.hand_value() == (4,[5])

# straight with two pairs
c1 = card("diamonds",11)
c2 = card("spades",10)
c3 = card("clubs",8)
c4 = card("hearts",9)
c5 = card("diamonds",10)
c6 = card("clubs",12)
c7 = card("diamonds",8)

poker26 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker26.hand_value() == (4,[12])

# straight with three of a kind
c1 = card("diamonds",11)
c2 = card("spades",10)
c3 = card("clubs",10)
c4 = card("hearts",9)
c5 = card("diamonds",10)
c6 = card("clubs",12)
c7 = card("diamonds",8)

poker27 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker27.hand_value() == (4,[12])

# three of a kind
c1 = card("clubs",10)
c2 = card("spades",11)
c3 = card("hearts",12)
c4 = card("spades",8)
c5 = card("clubs",7)
c6 = card("diamonds",7)
c7 = card("spades",7)

poker28 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker28.hand_value() == (3,[7,12,11])

# two pairs
c1 = card("clubs",10)
c2 = card("spades",10)
c3 = card("hearts",12)
c4 = card("spades",8)
c5 = card("clubs",7)
c6 = card("diamonds",7)
c7 = card("spades",3)

poker29 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker29.hand_value() == (2,[10,7,12])

# two pairs with a third pair
c1 = card("clubs",10)
c2 = card("spades",12)
c3 = card("hearts",12)
c4 = card("spades",3)
c5 = card("clubs",7)
c6 = card("diamonds",7)
c7 = card("spades",3)

poker30 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker30.hand_value() == (2,[12,7,10])

# single pair
c1 = card("clubs",10)
c2 = card("spades",10)
c3 = card("hearts",12)
c4 = card("spades",8)
c5 = card("clubs",4)
c6 = card("diamonds",7)
c7 = card("spades",3)

poker31 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker31.hand_value() == (1,[10,12,8,7])

# high card
c1 = card("clubs",10)
c2 = card("spades",2)
c3 = card("hearts",12)
c4 = card("spades",8)
c5 = card("clubs",4)
c6 = card("diamonds",7)
c7 = card("spades",3)

poker32 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker32.hand_value() == (0,[12,10,8,7,4])

print("All tests complete.\n")

## All possible hand variations
"""
Royal flush -> 1-5
    with no pair
    with one pair 
    with three of a kind
    full 7 cards

Straight flush -> 6-10
    with no pair
    with one pair
    with three of a kind
    full 7 cards

Four of a kind -> 11-13
    regular
    with pair
    with three of a kind

Full house -> 14-17
    two three of a kinds, no pair
    two three of a kind, pair
    
flush -> 18-23
    regular
    with pair
    with two pair
    with straight
    with trips

straight -> 24-27
    regular
    with pair
    with two pair
    with trips

three of a kind -> 28
    regular

two pair -> 29-30
    regular
    three pairs

one pair -> 31
    regular

high card -> 32
"""

## Random hand generator
import random as r
def generate_hand():

    # all possible suites
    suites = ("spades","hearts","clubs","diamonds")

    # all numbers, 14 is ace which is 1 and 14
    numbers = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    cards = []

    # generate 7 unique cards
    while len(cards) < 7:

        # random generation of card components
        suite = r.choice(suites)
        number = r.choice(numbers)
        newcard = card(suite,number)

        # ensure each card is unique
        if newcard not in cards:
            cards += [newcard]

    print(cards)

    # call poker_hand function from card_ranking_logic.py and use output to find hand strength
    poker_hand_test = poker_hand(cards[0],cards[1],cards[2],cards[3],cards[4],cards[5],cards[6]).hand_value()
    new_hand_val = []
    for item in poker_hand_test:
        new_hand_val += [item]
    hand_val_dict = {0:"High Card",1:"One Pair",2:"Two Pair",3:"Three of a Kind",4:"Straight",5:"Flush",6:"Full House",7:"Four of a Kind",
    8:"Straight Flush",9:"Royal Flush"}
    new_hand_val[0] = hand_val_dict[new_hand_val[0]]

    # print cleaned data from the output of poker_hand function
    print(new_hand_val)
    print("\n")
    return poker_hand(cards[0],cards[1],cards[2],cards[3],cards[4],cards[5],cards[6])

## Monte Carlo-esque simulator to see what the average hand value would be based on many trials
def run_hand_test(n):

    # call poker_hand function n times to get each value of hand and average them
    counter = 0
    total_hand_val = 0
    while counter != n:
        hand_value = generate_hand()
        total_hand_val += hand_value[0]
        counter += 1
    avg_hand_val = total_hand_val / n
    print(avg_hand_val)
    return avg_hand_val

# generate_hand()

## Comparison Tests
def comparison_tests(n):
    for num in range(n):
        
        # generate first random hand
        print("Hand 1")
        hand1 = generate_hand()
        # generate second random hand
        print("Hand 2")
        hand2 = generate_hand()
        # use or function that was overrided in class poker_hand
        hand1 | hand2
    return
comparison_tests(1)
