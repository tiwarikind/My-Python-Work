import random

#Global Variable
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


#Card Class
class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " +self.suit


#Deck Shuffle-Deal
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)


    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

#Player Remove card/Add Card/Extend Card to winner
class Player:

    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards) #Multiple cards
        else:
            self.all_cards.append(new_cards) #Single Cards

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'



#Create player
player_one=Player("One")
player_two=Player("Two")

#create Deck of 52 card and shuffle them
new_deck=Deck()
new_deck.shuffle()

#distribute them between 2 players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True #set the boolean for game to continue
round_num=0 #count the round of game

#loop the game
while game_on:
    round_num +=1
    print(f"round {round_num}")
    if len(player_one.all_cards)==0:
        print('Player one, out of card! Player Two win')
        game_on=False
        break
    if len(player_two.all_cards)==0:
        print('Player two, out of card! Player one win')
        game_on=False
        break

    #start A new Round - show the card to table
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    at_war=True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war =False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war=False
        else:
            print('WAR!!')
            if len(player_one.all_cards)<5:
                print("Player one unable to declare War")
                print ("Player Two wins")
                game_on=False
                break
            elif len(player_two.all_cards)<5:
                print("Player two unable to declare War")
                print ("Player one wins")
                game_on=False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
