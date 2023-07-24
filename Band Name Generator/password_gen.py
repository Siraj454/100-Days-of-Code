#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letter=random.sample(letters,nr_letters)
letter="".join(letter)
number=random.sample(numbers,nr_numbers)
number="".join(number)
#symbol
symbol=random.sample(symbols,nr_symbols)
symbol="".join(symbol)
password=str(letter+number+symbol)
print(password)
pass_list=[*password] #['q', 'U', 'B', '9', '%', '*'] #converts string to list
#pass_list=random.shuffle(pass_list)
print('random pass',pass_list)
#for i in range(len(pass_list)):
 #   pswd=random.choice(pass_list)
  #  random_password+=pswd
#print('radom pasword',random_password)
print('random through sampling')
random_pass_list=random.sample(pass_list,len(pass_list))
random_password=''.join(random_pass_list)
print('random Password is ',random_password)