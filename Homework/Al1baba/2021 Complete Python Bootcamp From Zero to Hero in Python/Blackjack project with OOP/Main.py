import game_logic as b


def hand_total(hand):
    # Getting the card value from string
    # print(hand)
    card_total = 0
    amount_of_aces = 0

    temp_list = str(hand).split("|")
    temp_list = list(filter(None, temp_list))
    temp_list = [x.split() for x in temp_list]      # Every card is one element in the list

    for num in range(len(temp_list)):
        card_total += int(temp_list[num][-1][1:-1])
        if int(temp_list[num][-1][1:-1]) == 1:
            amount_of_aces += 1

    total_value_str = f"{card_total} ({card_total + (10 * amount_of_aces)})"

    return total_value_str



def game():
    player1_bank = b.Currency("Sam", 500)
    player1_hand = b.Hand()
    house_hand = b.House()

    print(f"""
{player1_bank}    
    
The house hand is {house_hand}
--- Total {hand_total(house_hand)} ---
------------------------------------------------------
--- Total {hand_total(player1_hand)} ---
Your Hand is {player1_hand} 
""")


game()
