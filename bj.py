import random
i = 0
suit = ["C", "H", "S", "D"]
value_list = ["2", "3","4", "5", "6", "7", "8", "9", "10", "J", "Q","K","A"]
isdealer = False
space = "----------------------------------------------------"
hit_stand = ""
player_total = 0
player_cards = ""
#create BJ card
def randomcard():
    card = ""
    card += value_list[random.randint(0, len(value_list)-1)]
    card += suit[random.randrange(0, len(suit) - 1)]
    return card
#extracts value from the cargd
def evaluate():
    bj_card = randomcard()
    card = bj_card[0]
    if card.isnumeric():
        card = int(card)
        value = card
    elif card == "J" or "Q" or "K" or "A":
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
        total_value += value
    print(space)
    print(f"dealers cards: \nvalue:0 \n ........................................\nyour cards: {total_cards} \nvalue: {total_value}")
    hit_stand = input("HIT or STAND     ")
    while hit_stand != "h" and hit_stand != "s":
        hit_stand = input("input h for hit, S for stand")
    while hit_stand == "h":
        values_tp = evaluate()
        card = values_tp[1]
        value = values_tp[0]
        total_cards += card + " "
        total_value += value
        if total_value < 21:
            print(space)
            print(f"dealers cards: \nvalue:0 \n ........................................\nyour cards: {total_cards} \nvalue: {total_value}")
            hit_stand = input("HIT or STAND ")
            while hit_stand != "h" and hit_stand != "s":
                hit_stand = input("input h for hit, S for stand")
        elif total_value == 21:
            BJ = True
            print(f"dealers cards: \nvalue:0 \n ........................................\nyour cards: {total_cards} \nvalue: {total_value}")
            print("BLACKJACK!")
            break
        elif total_value > 21:
            print(space)
            print(f"dealers cards: \nvalue:0 \n ........................................\nyour cards: {total_cards} \nvalue: {total_value}")
            print(space)
            print("you lost!")
            lose = True
            break

        return (total_value, total_cards, BJ, lose)

def dealer_turn():
    val_total = 0
    card_total = ""
    card_valsuit = []
    player_value = yourturn()
    print(type(player_value[3]))
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
        print(type(card))
        print(type(card_value))
        print(card_value)
        val_total  += int(card_value)
        card_total += (f"{str(card)} ")
        if val_total >= 17:
            if val_total <= 21:
                if val_total >= player_total:
                    print(f"dealers cards: {card_total}\nvalue: {val_total} \n ........................................\nyour cards: {player_cards} \nvalue: {player_total}")
                    print("you lost!\n")
            else:
                print(f"dealers cards: {card_total}\nvalue: {val_total} \n ........................................\nyour cards: {player_cards} \nvalue: {player_total}")
                print("you won!\n")

dealer_turn()

