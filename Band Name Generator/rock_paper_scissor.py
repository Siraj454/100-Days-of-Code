rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
options=[rock,paper,scissors]
user_choice=int(input('what is your choice rock 0,paper 1 and scissor 2?'))
# 0 Rock wins against scissors 2.
#2 Scissors win against 1 paper.
# 1 Paper wins against rock 0.
computer_choice=random.randint(0,2)
if options[user_choice]==options[computer_choice]:
    print('Draw!!!!!!')
    print(f'Your chioce\n{options[user_choice]}\n Computer Choice {options[computer_choice]}')
elif user_choice==0 and computer_choice == 2:
    print('you Win!!!!!!')
    print(f'Your chioce\n{options[user_choice]}\n Computer Choice {options[computer_choice]}')
elif user_choice==2 and computer_choice == 0:
    print('you Loseee!!!!!!')
    print(f'Your chioce\n{options[user_choice]}\n Computer Choice {options[computer_choice]}')
elif user_choice>computer_choice:
    print('You Win')
    print(f'Your chioce\n{options[user_choice]}\n Computer Choice {options[computer_choice]}')
else:
    print('you lose')
    print(f'Your chioce\n{options[user_choice]}\n Computer Choice {options[computer_choice]}')