name='abbcderfg'
print(name.index('b'))


  print(emp_list)
            break
        else:
            print('word not present')
            break
    #print('game completed')
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in range(len(chosen_word)):
    if chosen_word[i]==guess:
        emp_list[i]=guess
        print('Word Present')
    else:
        print('Word Not Present')
        print(emp_list)
