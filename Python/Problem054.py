# In the card game poker, a hand consists of five cards and are ranked
# , from lowest to highest, in the following way:
# 
#     * High Card: Highest value card.
#     * One Pair: Two cards of the same value.
#     * Two Pairs: Two different pairs.
#     * Three of a Kind: Three cards of the same value.
#     * Straight: All cards are consecutive values.
#     * Flush: All cards of the same suit.
#     * Full House: Three of a kind and a pair.
#     * Four of a Kind: Four cards of the same value.
#     * Straight Flush: All cards are consecutive values of same suit.
#     * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# 
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# 
# If two players have the same ranked hands then the rank made up of 
# the highest value wins; for example, a pair of eights beats a pair 
# of fives (see example 1 below). But if two ranks tie, for example, 
# both players have a pair of queens, then highest cards in each hand 
# are compared (see example 4 below); if the highest cards tie then 
# the next highest cards are compared, and so on.
# 
# Consider the following five hands dealt to two players:
# 
# The file, poker.txt, contains one-thousand random hands dealt to 
# two players. Each line of the file contains ten cards (separated by 
# a single space): the first five are Player 1's cards and the last 
# five are Player 2's cards. You can assume that all hands are valid
# (no invalid characters or repeated cards), each player's hand is in 
# no specific order, and in each hand there is a clear winner.
# 
# How many hands does Player 1 win?

from copy import copy

HEARTS = 0
SPADES = 1
CLUBS = 2
DIAMONDS = 3

TWO = 0
THREE = 1
FOUR = 2
FIVE = 3
SIX = 4
SEVEN = 5
EIGHT = 6
NINE = 7
TEN = 8
JACK = 9
QUEEN = 10
KING = 11
ACE = 12

HIGH_CARD = 0
PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8

suits = {
        'H': HEARTS,
        'S': SPADES,
        'C': CLUBS,
        'D': DIAMONDS,
        }
ranks = {
        '2': TWO,
        '3': THREE,
        '4': FOUR,
        '5': FIVE,
        '6': SIX,
        '7': SEVEN,
        '8': EIGHT,
        '9': NINE,
        'T': TEN,
        'J': JACK,
        'Q': QUEEN,
        'K': KING,
        'A': ACE,
        }

class Card(object):
    def __init__(self, card_string):
        self.rank = ranks[card_string[0]]
        self.suit = suits[card_string[1]]
        self.string = card_string
    def __cmp__(self, other_card):
        if self.rank < other_card.rank:
            return -1
        if self.rank > other_card.rank:
            return 1
        return 0
    def __str__(self):
        return self.string

class Hand(object):
    def __init__(self, cards):
        self.cards = sorted([Card(card) for card in cards], reverse=True)
        self.hand_value = self.evaluate()

    def evaluate(self):
        if len(set(card.suit for card in self.cards)) == 1:
            flush = True
        else:
            flush = False

        if ( len(set( card.rank for card in self.cards ) ^ set([ACE, TWO, THREE, FOUR, FIVE])) == 0
                or all( (self.cards[i].rank == (self.cards[i+1].rank - 1)) for i in range(len(self.cards)-1) ) ):
            straight = True
        else:
            straight = False

        if straight or flush:
            self.active_cards = copy(self.cards)
            self.remaining_cards = []
            self.major_rank = None
            self.minor_rank = None
        if straight and flush:
            return STRAIGHT_FLUSH
        if flush:
            return FLUSH
        if straight:
            return STRAIGHT

        ranks = [ card.rank for card in self.cards ]
        distribution = dict((rank, ranks.count(rank)) for rank in set(ranks))
        four_sets = [ key for key in distribution.keys() if distribution.get(key) == 4 ]
        three_sets = [ key for key in distribution.keys() if distribution.get(key) == 3 ]
        pairs = [ key for key in distribution.keys() if distribution.get(key) == 2 ]

        if len(four_sets) == 1:
            self.major_rank = four_sets[0]
            self.minor_rank = None
            self.active_cards = [ card for card in self.cards if card.rank in four_sets ]
            self.remaining_cards = [ card for card in self.cards if card.rank not in four_sets ]
            return FOUR_OF_A_KIND

        if len(three_sets) == 1:
            self.major_rank = three_sets[0]
            if len(pairs) == 1:
                self.minor_rank = pairs[0]
                self.active_cards = copy(self.cards)
                self.remaining_cards = []
                return FULL_HOUSE
            self.minor_rank = None
            self.active_cards = [ card for card in self.cards if card.rank in three_sets ]
            self.remaining_cards = [ card for card in self.cards if card.rank not in three_sets ]
            return THREE_OF_A_KIND

        if len(pairs) == 2:
            self.major_rank = max(pairs)
            self.minor_rank = min(pairs)
            self.active_cards = [ card for card in self.cards if card.rank in pairs ]
            self.remaining_cards = [ card for card in self.cards if card.rank not in pairs]
            return TWO_PAIR

        if len(pairs) == 1:
            self.major_rank = pairs[0]
            self.minor_rank = None
            self.active_cards = [ card for card in self.cards if card.rank in pairs ]
            self.remaining_cards = [ card for card in self.cards if card.rank not in pairs]
            return PAIR
        
        self.active_cards = [self.cards[-1]]
        self.remaining_cards = self.cards[:-1]
        self.major_rank = self.active_cards[0].rank
        self.minor_rank = None
        return HIGH_CARD

    def __cmp__(self, other_hand):
        if self.hand_value > other_hand.hand_value:
            return 1
        if self.hand_value < other_hand.hand_value:
            return -1
        if self.major_rank > other_hand.major_rank:
            return 1
        if self.major_rank < other_hand.major_rank:
            return -1
        if self.minor_rank > other_hand.minor_rank:
            return 1
        if self.minor_rank < other_hand.minor_rank:
            return -1
        if self.active_cards > other_hand.active_cards:
            return 1
        if self.active_cards < other_hand.active_cards:
            return -1
        if self.remaining_cards > other_hand.remaining_cards:
            return 1
        if self.remaining_cards < other_hand.remaining_cards:
            return -1
        return 0

    def __str__(self):
        return ', '.join([str(card) for card in self.active_cards]) + ' (' + ', '.join([str(card) for card in self.remaining_cards]) + ') - ' + str(self.hand_value)

if __name__ == "__main__":
    player_1_wins = 0
    player_2_wins = 0
    ties = 0
    with open('poker.txt','r') as file:
        for line in file.readlines():
            cards = line.strip().split()
            player_1_hand = Hand(cards[:5])
            player_2_hand = Hand(cards[5:])

            if player_1_hand > player_2_hand:
                player_1_wins += 1
            elif player_1_hand < player_2_hand:
                player_2_wins += 1
            else:
                ties += 1
    print player_1_wins
