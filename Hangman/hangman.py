#Step 1 
import random
from replit import clear
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
print('chosen_word',chosen_word)
display=['-' for i in range(len(chosen_word)) ]
#print(display)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
choosen_len=len(chosen_word)

while choosen_len>0 and '-' in display:
    guess=input('guess a word: ').lower()
    clear() #
    #print(display)
    if guess in display:
        print('word already present')
    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess: 
                display[i]=guess
        print('Word found')
        choosen_len=choosen_len-1
    elif guess not in chosen_word:
            print('word not found')
            choosen_len=choosen_len-1
    #print(display)
    #print('Life Remaining',choosen_len)

    if '-' not in display:
        print('you won')
    if choosen_len==0 and '-' in display:
        print('you loose')
    #print('Life Remaining',choosen_len)
    print(display)
    print('Life Remaining',choosen_len)
    