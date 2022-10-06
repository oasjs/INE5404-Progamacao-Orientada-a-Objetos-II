# These classes are optimal for creating decks based off of the traditional 52 playing set, but it can be used to create other decks, such as the one used in the game Uno.

class Card():
    def __init__(self, suit=None, number=None, color=None, face=None) -> None:
        self.__suit = suit
        self.__number = number
        self.__color = color
        self.__face = face


class Deck():
    def __init__(self, *cards:Card) -> None:
        self.__cards = list(cards)
        self.__set_deck = [[None, 0]]*len(cards)


    def get_deck(self):
        print(self.__set_deck)

    def num_cards(self):
        for i in range(len(self.__set_deck)):
            self.__set_deck[i][0] = self.__cards[i]
            self.__set_deck[i][1] = int(input(f'How many cards of the {self.__set_deck[i][0]} type?' ))
        
    # The methods __get_card_num ad num_sort work to sort the deck by the number value of each card.
    def __get_card_num(self):
        for card in self.__cards:
            return card.__number

    def num_sort(self):
        self.__set_deck.sort(key=self.__get_card_num())

    def suit_sort():
        pass

ace_of_spades = Card("Spades", 1)
two_of_spades = Card("Spades", 2)
three_of_spades = Card("Spades", 3)
four_of_spades = Card("Spades", 4)
five_of_spades = Card("Spades", 5)

deck = Deck(ace_of_spades, two_of_spades, three_of_spades, four_of_spades, five_of_spades)
deck.num_cards()
deck.get_deck()

