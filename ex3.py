def percent_to_gpv(mark):
    '''(int) -> float
    Accepts a mark and calculates the corresponding GPA based on
    that mark and returns it
    
    REQ: mark >= 0
    REQ: mark <= 100
    
    >>>percent_to_gpv(85)
    4.0
    >>>percent_to_gpv(72)
    2.7
    >>>percent_to_gpv(50)
    0.7
    
    '''
    #Based on user mark, will return the corresponding GPA value, if the user
    #gets below a 50, it will return the final case which is a GPA of 0.0
    if (mark >= 85):
        return 4.0
    elif (mark >= 80):
        return 3.7
    elif (mark >= 77):
        return 3.3
    elif (mark >= 73):
        return 3.0
    elif (mark >= 70):
        return 2.7
    elif (mark >= 67):
        return 2.3
    elif (mark >= 63):
        return 2.0
    elif (mark >= 60):
        return 1.7
    elif (mark >= 57):
        return 1.3
    elif (mark >= 53):
        return 1.0
    elif (mark >= 50):
        return 0.7
    else:
        return 0.0    
    
def card_namer(cardName,suit):
    '''
    (string,string) -> string
    Given a single letter or number for card name, and a single letter
    for card suit, it will return the full name of the card
    
    >>> card_namer('K','D')
    'King of Diamonds'
    >>> card_namer('9','H')
    '9 of Hearts'
    >>> card_namer('A','T')
    'CHEATER!'

    
    '''
    #Calls upon the suit_namer function to get the full name of the
    #given card suit, if the input suit isn't valid, it will simply return
    #cheater and end the function
    cardSuit = suit_namer(suit)
    cardType = ""
    
    #Returns cheater if the card suit is not a valid card
    if (cardSuit == ('CHEATER!')):
        cardType = cardSuit  
    #checks the cardName that was inputted and gives the cardType the full name
    #of that card and inputs in the card suit as well
    elif (cardName == "A"):
        cardType = 'Ace' + cardSuit
    elif (cardName == "K"):
        cardType = 'King ' + cardSuit
    elif (cardName == "Q"):
        cardType = 'Queen ' + cardSuit
    elif (cardName == "J"):
        cardType = 'Jack ' + cardSuit
    elif (cardName == "T"):
        cardType = '10 ' + cardSuit
    elif (cardName == "9 "):
        cardType = cardName + cardSuit
    elif (cardName == "8 "):
        cardType = cardName + cardSuit
    elif (cardName == "7 "):
        cardType = cardName + cardSuit
    elif (cardName == "6 "):
        cardType = cardName + cardSuit
    elif (cardName == "5 "):
        cardType = cardName + cardSuit
    elif (cardName == "4 "):
        cardType = cardName + cardSuit
    elif (cardName == "3 "):
        cardType = cardName + cardSuit
    elif (cardName == "2 "):
        cardType = cardName + cardSuit
    else:
        cardType = cardSuit #cardType has no value if not in the parameters given
        
    return cardType

def suit_namer(suit):
    '''
    (string) -> string
    
    given a shorthand version of a card suit, will return the complete
    name of a card suit, if the suit isn't valid, it will return cheater
    
    >>>suit_namer("D")
    " of Diamonds"
    >>>suit_namer("C")
    " of Clubs"
    >>>suit_namer("T")
    'CHEATER!'
    '''
    Suitname = ""
    
    if (suit == "D"):
        Suitname = "of Diamonds"
    elif (suit == "C"):
        Suitname = "of Clubs"
    elif (suit == "H"):
        Suitname = "of Hearts"
    elif (suit == "S"):
        Suitname = "of Spades"
    else:
        Suitname = ('CHEATER!') #returns cheater if the card suit isn't valid
        
    return Suitname
    