from deck import Deck
from hand import Hand



class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        while self.player.balance > 0:
            start = input(f"You are starting with ${self.player.balance}. Would you like to play a hand?")
            if start.lower() == "y" or start.lower() == "yes":
                self.start_round()
            elif start.lower() == "n" or start.lower() == "no":
                print(f"You left the game with ${self.player.balance}.")
        else:
            print("You've ran out of money. Please restart this program to try again. Goodbye.")

    def start_round(self):
        self.place_bet()
        self.dealing_starting_card()

        if self.black_jack():
            return
        
        player_lost = self.player_turn()
        if player_lost:
            print(f"Your hand value is over 21 and you lose ${self.bet} :(")
            return
        
        dealer_lost = self.dealer_turn()
        if dealer_lost:
            self.player.balance += self.bet * 2
            print(f"The dealer busts, you win ${self.bet} :)")
            return
        
        self.determine_winner()
        self.reset_round()
    
    def reset_round(self):
        self.player.hand = None
        self.dealer.hand = None
        self.bet = None
        self.deck = Deck()

    def determine_winner(self):
        player_value = self.player.hand.get_value()
        dealer_value = self.dealer.hand.get_value()

        if dealer_value > player_value:
            print(f"The dealer wins, you lose ${self.bet} :(")
        elif dealer_value < player_value:
            self.player.balance += self.bet * 2
            print(f"You win ${self.bet}")
        else:
            self.player.balance += self.bet
            print(f"You tie. Your bet has been returned.")



    def place_bet(self):
        while True:
            bet = float(input("Place your bet:"))
            if bet > self.player.balance:
                print("You do not have sufficient funds.")
            elif bet < self.MINIMUM_BET:
                print("The minimum bet is $1.")
            else:
                self.bet = bet
                self.player.balance -= bet
                break
        
    def dealing_starting_card(self):
        self.player.hand = Hand(self.deck.deal(2))
        self.dealer.hand = Hand(self.deck.deal(2))
        self.dealer.hand.cards[1].hidden = True
        print(f"You are dealt: {self.player.get_str_hand()}")
        print(f"The dealer is dealt: {self.dealer.get_str_hand()}")
        self.dealer.hand.cards[1].hidden = False

    
    def black_jack(self):
        if self.player.hand.get_value() != 21:
            return False
        
        print(f"The dealer has: {self.dealer.get_str_hand()}")
        if self.dealer.hand.get_value() == 21:
            self.player.balance += self.bet
            print("Both you and the dealer have Blackjack, you tie. Your bet has been returned.")
            return True

        self.player.balance += (self.bet * 2.5)
        print(f"Blackjack! You win ${self.bet * 2.5}")
        return True
    
    def player_turn(self):
        while True:
            respond = input("Would you like to hit or stay?")
            if respond == "hit":
                new_card = self.deck.deal(1)[0]
                self.player.hit(new_card)
                print(f"You are dealt: {str(new_card)}")
                print(f"You now have: {self.player.get_str_hand()}")

                if self.player.hand.get_value() > 21:
                    return True

            elif respond == "stay":
                return False
            else:
                print("That is not a valid option. Pls, respond hit or stay.")

    def dealer_turn(self):
        print(f"The dealer has: {self.dealer.get_str_hand()}")
        while self.dealer.hand.get_value() <= 16:
            new_card = self.deck.deal(1)[0]
            self.dealer.hit(new_card)
            print(f"Dealer hits and is dealt: {str(new_card)}")
            print(f"Dealer now have: {self.dealer.get_str_hand()}")
        
        if self.dealer.hand.get_value() > 21:
            return True
        
        return False
