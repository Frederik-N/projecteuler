# Problem 54 - Poker Hands
#The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space):
#  the first five are Player 1's cards and the last five are Player 2's cards.
#  You can assume that all hands are valid (no invalid characters or repeated cards), 
# each player's hand is in no specific order, and in each hand there is a clear winner.

# Open the file and put it into a string

# This solution cannot decide 2 of the hands yet, and one of these player 1 wins (full house not implemented, and hands with same two pairs)

from collections import defaultdict

# dict for rank of cards
card_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
player1wins = 0
player2wins = 0

def hasPair(value, playercards, cards):
    removeCharacters = ["S", "C", "D", "H", " "]
    for character in removeCharacters:
        playercards = playercards.replace(character,"")
    rankcount = defaultdict(lambda:0)
    card = [x[0] for x in playercards]
    for y in card:
        rankcount[y] += 1
    for k,v in rankcount.items():
        if(v==2):
            print(k, "key")
            return 2, str(k)
    return value, cards

def hasFourOfKind(value, playercards, cards):
    removeCharacters = ["S", "C", "D", "H", " "]
    for character in removeCharacters:
        playercards = playercards.replace(character,"")
    rankcount = defaultdict(lambda:0)
    card = [x[0] for x in playercards]
    for y in card:
        rankcount[y] += 1
    for x in set(rankcount.values()):
        if(x==4):
            return 8, playercards
    return value, cards

def hasFullHouse(value, playercards, cards):
    return value, cards

def hasThreeOfKind(value, playercards, cards):
    removeCharacters = ["S", "C", "D", "H", " "]
    for character in removeCharacters:
        playercards = playercards.replace(character,"")
    rankcount = defaultdict(lambda:0)
    card = [x[0] for x in playercards]
    for y in card:
        rankcount[y] += 1
    
    for x in set(rankcount.values()):
        if(x==3):
            return 4, playercards

    return value, cards

def hasTwoPairs(value, playercards, cards):
    removeCharacters = ["S", "C", "D", "H", " "]
    for character in removeCharacters:
        playercards = playercards.replace(character,"")
    rankcount = defaultdict(lambda:0)
    card = [x[0] for x in playercards]
    for y in card:
        rankcount[y] += 1
    count = 0
    for x in list(rankcount.values()):
        if(x==2):
            count +=1
            if(count == 2):
                return 3, playercards

    return value, cards

def hasRoyalFlush(value, playercards, cards):
    if('TH' in playercards and 'JH' in playercards and 'QH' in playercards and 'KH' in playercards and 'AH' in playercards):
        return 10, playercards
    if('TD' in playercards and 'JD' in playercards and 'QD' in playercards and 'KD' in playercards and 'AD' in playercards):
        return 10, playercards
    if('TC' in playercards and 'JC' in playercards and 'QC' in playercards and 'KC' in playercards and 'AC' in playercards):
        return 10,playercards
    if('TS' in playercards and 'JS' in playercards and 'QS' in playercards and 'KS' in playercards and 'AS' in playercards):
        return 10,playercards
    return value, cards

def hasStraight(value, playercards, cards):
    removeCharacters = ["S", "C", "D", "H", " "]
    for character in removeCharacters:
        playercards = playercards.replace(character,"")
    #todo check if playercards is straight from 5 ranks close to each other
    rankcount = defaultdict(lambda:0)
    card = [x[0] for x in playercards]
    for y in card:
        rankcount[y] += 1
    cardranks = [card_dict[x] for x in card]
    if(max(cardranks)-min(cardranks) ==4 and len(set(rankcount.values()))==1):
        return 5, playercards
    return value, cards

def hasFlush(value, playercards, cards):
    countH, countC, countD, countS = 0,0,0,0
    for x in playercards:
        if(x == 'H'):
            countH += 1
        elif(x == 'S'):
            countS += 1
        elif(x == 'C'):
            countC += 1
        elif(x == 'D'):
            countD += 1
    if((countH or countC or countD or countS) == 5):
        return 6, playercards
    return value, cards


def hasStraighFlush(value, playercards, cards):
    #check if containing a straight flush by checking if it has both a straight and flush
    if(hasStraight(value, playercards, cards)[0] ==5 and hasFlush(value, playercards, cards)[0]==6):
        return 9, playercards
    return value, cards
        
def checkHighestCard(cards1, cards2):
    if not cards1 or not cards2:
        return 0
    removeCharacters = ["S", "C", "D", "H", " "]
    for character in removeCharacters:
        cards1 = cards1.replace(character,"")
        cards2 = cards2.replace(character,"")
    card1 = [x[0] for x in cards1]
    card2 = [x[0] for x in cards2]
    cardranks1 = [card_dict[x] for x in card1]
    cardranks2 = [card_dict[x] for x in card2]
    print(cardranks1,cardranks2, "here")
    if(max(cardranks1)>max(cardranks2)):
        return 1
    elif(max(cardranks2)>max(cardranks1)):
        return 2
    else:
        mcards1 = cards1.replace(str(max(cardranks1)), "")
        mcards2 = cards2.replace(str(max(cardranks2)), "")
        print(mcards1, mcards2, "new cards")
        checkHighestCard(mcards1, mcards2)

def onlyHighCardCheck(player1cards, player2cards, valuePlayer1, valuePlayer2):
    global player1wins, player2wins
    if(valuePlayer1 == 0 and valuePlayer2 == 0):
        checkHighest = checkHighestCard(player1cards, player2cards)
        if(checkHighest==1):
            print("Player1 wins with high card", x)
            player1wins += 1
        elif(checkHighest==2):
            print("Player2 wins with high card", x)
            player2wins += 1

#assigns a value to the cards from 0-10 depending on the rules
def valueOfCards(playercards):
    value, cards = 0, playercards
    value, cards = hasPair(value, playercards, cards)
    value, cards = hasTwoPairs(value, playercards, cards)
    value, cards = hasThreeOfKind(value, playercards, cards)
    value, cards = hasStraighFlush(value, playercards, cards)
    value, cards = hasStraight(value, playercards, cards)
    value, cards = hasFlush(value, playercards, cards)
    value, cards = hasFullHouse(value, playercards, cards)
    value, cards = hasFourOfKind(value, playercards, cards)
    value, cards = hasRoyalFlush(value, playercards, cards)
    # todo add additional rules / functions


    return value, cards


#save the data of poker hands to a string
datastring = ""
datafile = open('p054_poker.txt',"r")
if(datafile.mode == 'r'):
    datastring = datafile.read()
game = datastring.split('\n')
game = game[0:len(game)-1]
removeCharacters = [" "]

count = 0
for x in game:
    count += 1
    print("Game:", count)
    player1cards = x[:14]
    player2cards = x[15:]

    #for character in removeCharacters:
    #    player1cards = player1cards.replace(character,"")
    #    player2cards = player2cards.replace(character,"")
    
    # check value of cards
    valuePlayer1, cards1 = valueOfCards(player1cards)
    valuePlayer2, cards2 = valueOfCards(player2cards)
    
    print("CARDS OF PLAYER 1:", player1cards, "VALUE:", valuePlayer1)
    print("CARDS OF PLAYER 2:", player2cards, "VALUE:", valuePlayer2)
    # no better than high cards, check highest card, TODO recursive check next highest card
    onlyHighCardCheck(player1cards, player2cards, valuePlayer1, valuePlayer2)

    # if value is the same, check who has best rank cards
    if(valuePlayer1 == valuePlayer2 and (valuePlayer1 != 0 and valuePlayer2 != 0)):
        print(cards1, cards2)
        checkHighest = checkHighestCard(cards1, cards2)
        if(checkHighest==0):
            onlyHighCardCheck(player1cards, player2cards, valuePlayer1, valuePlayer2)
        if(checkHighest==1):
            print("Player1 wins with high card", x)
            player1wins += 1
        elif(checkHighest==2):
            print("Player2 wins with high card", x)
            player2wins += 1

    if(valuePlayer1>valuePlayer2):
        print("Player1 wins", x)
        player1wins += 1
    elif(valuePlayer2>valuePlayer1):
        print("Player2 wins", x)
        player2wins += 1
print("player1:", player1wins, "player2:", player2wins, "decided games:", player1wins+player2wins)

