
import random
import os
# easy level contains 5 attempts
def game(computer_choice):
    user_guess=int(input('Guess a num:'))
    if user_guess<computer_choice:
        return 'Too Low'
    if user_guess>computer_choice:
        return 'Too High'
    if user_guess==computer_choice:
        return 0
def play_game():
    numbers=[i for i in range(1,101)]
    computer_choice=random.choice(numbers)
    # for easy level tries should be 5
    print('Welcome to Guessing Game....')
    print('Computer is guessing between 1 and 100')
    level=int(input('Choose Dificulty 1 for easy 2 for hard: '))
    
    if level==1:
        num_attempts=10
    else:
        num_attempts=5
    print('num of attempts:',num_attempts)

            
    while num_attempts>0:
        result=game(computer_choice)
        if result==0:
            print('You Won')
            break
        print(result)
        num_attempts=num_attempts-1
        print('remaining attempts.....:',num_attempts)
    if num_attempts==0:
        print('You loose all attempts')
    
active=True
while active:
    os.system('cls')
    play_game()
    play_again=int(input('would you like to play again YES:1 No:0 '))
    if play_again==0:
        print('thanks playing.......')
        active=False

    