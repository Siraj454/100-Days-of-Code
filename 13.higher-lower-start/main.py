# import Data and libraries
from game_data import data
import random
data=data[:5]

# Data Format looks like
''' [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    }]'''

# Print Required output for a single dictionary
#print(f"Compare A: {data[1]['name']}, {data[1]['description']},from {data[1]['country']}")

## All Unique Pairs
pairs = []

for i in range(len(data)):
    for j in range(i+1, len(data)):
        pairs.append([data[i], data[j]])

#print(pairs)

# Pick to two random people from the list 
PAIRS=[]
def selected_pair():
    persons=[]
    for i in range(2):
        persons.append(random.choice(data))
    while persons[0]==persons[1]:
        person_a=random.choice(data)
        person_b=random.choice(data)
        persons=[person_a,person_b]
    return persons
def picked_pair():
    pair=random.choice(pairs)
    return pair

def compare_(pair):
    #persons=selected_pair()
    persons=pair
    a=persons[0]
    b=persons[1]
    if a['follower_count']>b['follower_count']:
        correct_answer='a'
    elif a['follower_count']<b['follower_count']:
        correct_answer='b'
    user_choice=input('Who is the Winner A or B:')
    user_choice=user_choice.lower()
    # if user_choice=='a' and a['follower_count']>b['follower_count']:
    #     correct_answer=True
    # elif user_choice=='a' and a['follower_count']<b['follower_count']:
    #     correct_answer=False
    #print(correct_answer)
    #print('a',a)
    #print('b',b)
    if user_choice==correct_answer:
        return 1
    elif user_choice!=correct_answer:
        return 0

#PAIRS.append(persons)
def game_():
    scores=0
    active=True
    while active:
        pair=picked_pair()
        print(pair)
        pairs.pop(pair)
        ans=compare_(pair) 
        if ans==1:
            print('Correct Answer')
            scores=scores+1
        else:
            print('Wrong Answer')
            active=False
    print('total scores',scores)
game_()

##Notes*****************
'''functionality to be added: pair checking ,pairs shouldn't repeat 
   game_over: all pairing done, user got all correct answrs and no more pair left
   better print statement showing names of entities to be compared'''