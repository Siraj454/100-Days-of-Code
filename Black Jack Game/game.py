import random
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# at the start of the game

#rules: if score= 21 blackjayck, if user score and computer score=21 draw
# user score higher than 21 , lose
# on pass computer will play until score is <17, i
# if computer score greater than 17 and greater than user , comp win
# any time user score equals comp score draw.

def calculate_score(cards):
    #return zero if black jack
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score,comp_score):
    if user_score==comp_score:
        print('Its a Draw')
    elif user_score==0:
        print('User Win, blackjack')
    elif comp_score==0:
        print('Comp Win, black jack')
    elif user_score>21:
        print('Comp Win, user went over')
    elif comp_score>21:
        print('User Wins,comp went over')
    elif user_score>comp_score and user_score<22:
        print('User Win')
    else:
        print('Comp Win')
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card


user_cards=[]
comp_cards=[]    

for i in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

game_over=False


while not game_over:

    user_score=calculate_score(user_cards)
    comp_score=calculate_score(comp_cards)
    print('User cards are',user_cards)
    print('Computer first card is ',comp_cards[0])
    if user_score==0 or comp_score==0 or user_score>21:
        game_over=True

    else:
        user_input=input('hit ,pass: ')
        if user_input=='hit':
            user_cards.append(deal_card())
        else:
            game_over=True


while comp_score>0 and comp_score<17:
    comp_cards.append(deal_card())
    comp_score=calculate_score(comp_cards)
    

print(f'User Cards:{user_cards}, User Score {user_score}')
print(f'Comp Cards:{comp_cards}, Comp Score {comp_score}')
compare_score(user_score,comp_score)


