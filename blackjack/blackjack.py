import random
#import tkinter as tk

cards = [1,2,3,4,5,6,7,8,9,10]
hand_dealer = [random.choice(cards),random.choice(cards)]
hand_player = [random.choice(cards),random.choice(cards)]

def draw_card(who):
    global hand_dealer,hand_player
    if who == 'dealer': 
        hand_dealer = hand_dealer + [random.choice(cards)]
        return hand_dealer
    if who == 'player': 
        hand_player = hand_player + [random.choice(cards)]
        print(hand_player)

def main_game():
#    root = tk.Tk()
#    root.title('BlackJack')
#    WIDTH, HEIGHT = 900,500
#    canvas = tk.Canvas(root, bg = '#FFFFFF',height=HEIGHT,width=WIDTH).pack()
#    frame = tk.Frame(canvas,bg='#A1B2C3').place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
#    frame_dealer = tk.Frame(frame,bg='#ABCDEF').place(relx=0.15,rely=0.2,relwidth=0.3,relheight=0.5)
#    frame_palyer = tk.Frame(frame,bg='#ABCDEF').place(relx=0.55,rely=0.2,relwidth=0.3,relheight=0.5)
#    blackjack_label = tk.Label(root, text='BlackJack',bg='#A1B2C3',font='Bold 16').place(relx=0.375,rely=0.05,relwidth=0.25,relheight=0.1)
#    label_dealer = tk.Label(frame_dealer, text = f'{hand_dealer}').place(relx=0.2,rely=0.25,relwidth=0.2,relheight=0.1)

#    root.mainloop()
    print(f'\nDealer {hand_dealer}   Player{hand_player}')

    while sum(hand_dealer) < 16:
        draw_card('dealer')
    print(f"Dealer's hand: {hand_dealer}, Dealer points: {sum(hand_dealer)}")

    if sum(hand_dealer)>21: 
        print('Dealer has busted!\nPLAYER WINS\n ')
        return

    while sum(hand_player)  < 21:
        choice = input('Does player want another card? yes/no --->  ')
        if choice == 'yes':
            draw_card('player')
        else:
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
    again = input('Want to play again? yes/no --->  ')
    if again == 'yes':
        hand_dealer = [random.choice(cards),random.choice(cards)]
        hand_player = [random.choice(cards),random.choice(cards)]
        main_game()
    else: 
        print('Thanks for playing!')
        break