# Memory Game
"""
This program is a cyber-themed memory matching game.
The objective is to find all matching pairs of cards.

All cards start face-down. The player selects two card positions.
If the selected cards match, they remain revealed.
If they do not match, they are hidden again after a short delay.

The game continues until all cards are revealed.

This program uses:
- Loops to keep the game running
- Lists to store cards and cybersecurity terms
- User input for gameplay
- Object-Oriented Programming (OOP) with Card, Deck, and MemoryGame classes
"""

import random
import time


def clear_screen():
    # Clears the screen by printing many blank lines
    # This prevents the player from seeing previous card values
    print("\n" * 100)


class Card:
    def __init__(self, value):
        # Initializes a card with a value(cybersecurity term) and hidden state
        self.value = value
        self.revealed = False

    def __str__(self):
        # Returns the card value if revealed, otherwise shows a "?"
        if self.revealed:
            return str(self.value)
        else:
            return "?"


class Deck:
    def __init__(self, list_of_terms):
        # Creates pairs of cards using the given list of cybersecurity terms
        # Doubles each term so it could appear twice for matching
        self.cards = [Card(value) for value in list_of_terms] + [Card(value) for value in list_of_terms]
        # Randomly shuffles the cards
        random.shuffle(self.cards)

    def deck_arrangement(self, columns):
        # Displays the cards in a grid format with a given number of columns

        print("\n" + "-" * (columns * 15))  # Top border

        # Loops through the deck in steps equal to the number of columns
        for i in range(0, len(self.cards), columns):
            row_has_cards = False
            row = "|"

            for j in range(columns):
                index = i + j

                # Ensures the index is within the list length
                if index < len(self.cards):
                    row_has_cards = True
                    # Displays card number and its value (or ? if hidden)
                    row += f" {index + 1}:{self.cards[index]} |"
                else:
                    # Adds empty spacing to keep grid alignment
                    row += " " * 15

            # Only print rows that contain cards
            if row_has_cards:
                print(row)
                print("-" * (columns * 15))

    def reveal(self, idx):
        # Reveals a card at the given index
        self.cards[idx].revealed = True

    def is_match(self, a, b):
        # Checks if two cards have the same value
        return self.cards[a].value == self.cards[b].value


class MemoryGame:
    def __init__(self):
        # List of cybersecurity-related terms used in the game
        cybersecurity_terms = [
            "Phishing", "IP-Address", "MAC-Address",
            "Firewall", "Motherboard", "Ports"
        ]

        # Creates the deck and sets grid column size
        self.deck = Deck(cybersecurity_terms)
        self.columns = 4

    def play(self):
        # Main game loop runs while at least one card is still hidden
        while any(not card.revealed for card in self.deck.cards):
            clear_screen()
            print("=== CyberSecurity Memory Match ===")

            # Display the current board
            self.deck.deck_arrangement(self.columns)

            try:
                print("\n")
                first_card = int(input("Pick FIRST card: ")) - 1
                print()
                second_card = int(input("Pick SECOND card: ")) - 1
            except ValueError:
                # Handles non-numeric input
                continue

            # Validation checks
            if first_card == second_card:
                print("Please choose two different numbers.")
                time.sleep(3)
                continue

            if not (0 <= first_card < len(self.deck.cards)) or \
               not (0 <= second_card < len(self.deck.cards)):
                print("Invalid card number.")
                time.sleep(3)
                continue

            if self.deck.cards[first_card].revealed or \
               self.deck.cards[second_card].revealed:
                print("One or both cards are already revealed.")
                time.sleep(3)
                continue

            # Reveal selected cards
            self.deck.cards[first_card].revealed = True
            self.deck.cards[second_card].revealed = True

            print("\n" * 6 + "You flipped:\n")
            self.deck.deck_arrangement(self.columns)

            # Check for match
            if self.deck.cards[first_card].value == self.deck.cards[second_card].value:
                print("\nYou found a match!\n")
                time.sleep(2)
            else:
                # Hide cards again if they don't match
                self.deck.cards[first_card].revealed = False
                self.deck.cards[second_card].revealed = False
                print("✘ Not a match.")
                print("You have 5 seconds to memorize...")
                time.sleep(5)

        # End of game message
        print("You have revealed all cards! Good job!")


# Starts the game 
if __name__ == "__main__":
    MemoryGame().play()







