import random

cards = [1,2,3,4,5,6,7,8,9,10]
hand_dealer = [random.choice(cards),random.choice(cards)]
hand_player = [random.choice(cards),random.choice(cards)]

def draw_card(who):
    global hand_dealer,hand_player
    if who == 'dealer': 
        hand_dealer = hand_dealer + [random.choice(cards)]
        print(f'Dealer {hand_dealer}')
    if who == 'player': 
        hand_player = hand_player + [random.choice(cards)]
        print(hand_player)

def main_game():
    print(f'\nDealer {hand_dealer}   Player{hand_player}')

    while sum(hand_dealer) < 16:
        draw_card('dealer')
    print(f"Dealer's hand: {hand_dealer}, Dealer points: {sum(hand_dealer)}")

    if sum(hand_dealer)>21: 
        print('Dealer has busted!\nPLAYER WINS\n')
        return

    while sum(hand_player)  < 21:
        choice = input('Does player want another card?')
        if choice == 'yes':
            draw_card('player')
        elif choice == 'no': 
            print(f"Player's hand is {hand_player}, Player has {sum(hand_player)} points.")
            break

    if sum(hand_dealer) >= sum(hand_player) or sum(hand_player) > 21:
        print(f'Dealer points: {sum(hand_dealer)}\nPlayer points: {sum(hand_player)}')
        print('DEALER WINS\n')
    elif sum(hand_player)>sum(hand_dealer):
        print(f'Dealer points: {sum(hand_dealer)}\nPlayer points: {sum(hand_player)}')
        print('PLAYER WINS\n')

main_game()

while True:
    again = input('Want to play again?')
    if again == 'yes':
        hand_dealer = [random.choice(cards),random.choice(cards)]
        hand_player = [random.choice(cards),random.choice(cards)]
        main_game()
    else: 
        print('Thanks for playing!')
        break