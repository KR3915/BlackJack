import random
isplaying = True
i = 0
suit = ["C", "H", "S", "D"]
value_list = ["2", "3","4", "5", "6", "7", "8", "9", "10", "J", "Q","K","A"]
isdealer = False
space = "----------------------------------------------------"
hit_stand = ""
player_total = 0
player_cards = ""
balance = 1000
win = False
#create BJ card
def randomcard():
    card = ""
    card += value_list[random.randint(5, len(value_list)-1)]
    card += suit[random.randrange(0, len(suit) - 1)]
    return card
#extracts value from the cargd
def evaluate():
    bj_card = randomcard()
    card = bj_card[0]
    if card.isnumeric():
        value = int(card)
    elif card == "A":
     value = 11
    elif card == "J" or "Q" or "K" :
        value = 10
    return (value, bj_card)
#your turn
def yourturn():
    total_cards = ""
    total_value = 0
    BJ = False
    lose = False
    #deal first two cards
    for i in range(2):
        values_tp = evaluate()
        card = values_tp[1]
        value = values_tp[0]
        total_cards += card + " "
        #ace set if 1 or 11
        if value == 11 and value + total_value > 21:
            value = 1
        total_value += value
    print(space)
    print(f"dealers cards: \nvalue:0 \n\nyour cards: {total_cards} \nvalue: {total_value}")
    print(f"\n{space}")
    hit_stand = input("HIT or STAND?\n")
    hit_stand = hit_stand.lower()
    while hit_stand != "h" and hit_stand != "s":
        hit_stand = input("invalid input, input H for hit or S for stand")
        hit_stand = hit_stand.lower()
    #HIT
    while hit_stand == "h":
        values_tp = evaluate()
        card = values_tp[1]
        value = values_tp[0]
        total_cards += card + " "
        total_value += value

        #BLACKJACK
        if total_value == 21:
            BJ = True
            print(f"dealers cards: \nvalue:0 \n\nyour cards: {total_cards} \nvalue: {total_value}")
            print("BLACKJACK!")
            return (total_value, total_cards, BJ, lose)
            break
        #under 21
        elif total_value < 21:
            print(space)
            print(f"dealers cards: \nvalue:0 \n\nyour cards: {total_cards} \nvalue: {total_value}")
            print(space)
            hit_stand = input("HIT or STAND ")
            hit_stand = hit_stand.lower()
            while hit_stand != "h" and hit_stand != "s":
                hit_stand = input("invalid input. type S for Stand or H for Hit")
                hit_stand = hit_stand.lower()
        #over 21
        elif total_value > 21:
            print(space)
            print(f"dealers cards: \nvalue:0 \n\nyour cards: {total_cards} \nvalue: {total_value}")
            print(space)
            print("you lost!")
            lose = True
            return (total_value, total_cards, BJ, lose)
            break

    print(space)
    return (total_value, total_cards, BJ, lose)
#turn of the dealer
def dealer_turn():
    val_total = 0
    playerislose = False
    card_total = ""
    card_value = []
    card_valsuit = []
    player_value = yourturn()
    playerislose = player_value[3]
    playesisBJ = player_value[2]
    player_cards = str(player_value[1])
    player_val = int(player_value[0])
    while val_total <= 21:
        if playerislose == True or playesisBJ == True:
            break
        card_valsuit = evaluate()
        card = str(card_valsuit[1])
        card_value = int(card_valsuit[0])
        if card_value == 11 and val_total + card_value > 21:
            value = 1
        val_total  += int(card_value)
        card_total += (f"{str(card)} ")
        if val_total >= 17:
            if val_total <= 21:
                if val_total >= player_val:
                    print(f"dealers cards: {card_total}\nvalue: {val_total} \n\nyour cards: {player_cards} \nvalue: {player_val}")
                    print("you lost!\n")
                    win = False
                    return win
                else:
                    print(f"dealers cards: {card_total}\nvalue: {val_total} \n\nyour cards: {player_cards} \nvalue: {player_val}")
                    print("you win!\n")
                    win = True
                    return win
            else:
                print(f"dealers cards: {card_total}\nvalue: {val_total}\n\nyour cards: {player_cards} \nvalue: {player_val}")
                print("you won!\n")
                win = True
                return win
#game
def game():
    balance = 1000
    print(f"WELCOME TO BLACKJACK!                        ballance:{balance}\n")
    bet = (input("\nPLACE YOUR BET(input x for game to end or r for Rules) \n"))
    bet = str(bet)
    while isplaying == True:    
        if balance==0:
            print("your balance is zero")
            break
        
        #betting
        while not bet.isalpha() and bet and not bet.isnumeric():
            if bet.isnumeric():
               if int(bet)<balance:
                bet = (input("\ninsuficient funds please enter valid bet\n"))
               elif bet<0:
                bet = (input("\ncant bet a negative number\n"))  
               else:
                 bet = int(bet)  
            elif bet.isalpha():
                bet = str(bet)
                bet = str(bet.lower())
            else:
                print("enter valid input!")
        if bet == "x":
                print(f"thank you for playing! your final balance: {balance}")
                break
        elif bet == "r":
                print("Try to get 21 or as close as possible without going over.\nNumber cards = their number, face cards = 10, Ace = 1 or 11.\nYou get 2 cards. You can hit (get more) or stand (stop).\nDealer must hit until 17 or more.\nClosest to 21 wins!\n\n\n\n\n\n\n\n")
                
                
        win = dealer_turn()
        if win == True:
            balance += int(bet)
        else:
            balance = balance - int(bet)
        bet = input(f"\nPLACE YOUR BET(input X for game to end R for Rules)                         ballance:{balance}\n")
        bet = str(bet)
game()

