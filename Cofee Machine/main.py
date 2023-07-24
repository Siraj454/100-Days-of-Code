MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_price={'espresso':1.50,'latte':2.50,'cappuccino':3.0}
coins={'penny':0.01,'nickel':0.05,'dime':0.10,'quarter':0.25}
coffees=['espresso','latte','cappuccino']
total_amount=0


#function for checking resources
def resource_available(user_input):
    if  resources['water']>=MENU[user_input]['ingredients']['water'] and \
    resources['milk']>=MENU[user_input]['ingredients']['milk'] and \
    resources['coffee']>=MENU[user_input]['ingredients']['coffee']:
        return True
    else:
        return False

# function for coins 
def enough_coins(user_response,coins_total):
    if coins_total<coffee_price[user_response]:
        return False
    else:
        return True


#3.5 if coffe made deduct resources
def deduct_resources(coffee):
    resources['water']=resources['water']-MENU[coffee]['ingredients']['water']
    resources['milk']=resources['milk']-MENU[coffee]['ingredients']['milk']
    resources['coffee']=resources['coffee']-MENU[coffee]['ingredients']['coffee']

## change money add and give back
def deduct_money(user_response,coins_total,total_amount):
    change=coins_total-coffee_price[user_response] # calculate change
    total_amount=total_amount+coins_total # add all amount in cash box
    total_amount=total_amount-change # return change from the cash box
    return (change,total_amount)
## Create a report function
def report():
     print(f"water:{resources['water']}")
     print(f"milk:{resources['milk']}")
     print(f"cofee:{resources['coffee']}")
     print(f"Amount:{total_amount}")
def print_bill():
    print("***************Order Details*****************")
    print(f'Your Order for {user_response}......')
    print(f'Amount Paid: {coins_total}')
    print(f"Unit Price: {coffee_price[user_response]}")
    print(f"Change amount {change}$")
    print("Thanks for coming---Enjoy Your Coffee...........")

## todo1: Ask user their choice
machine_on=True
while machine_on:
    user_response=input(f"What would you like? (espresso/latte/cappuccino):")
    if user_response=='report':
        report()
    elif user_response=='off':
        machine_on=False
    elif user_response in coffees:
        #1.check resources if avaialble , then ask the user to enter the coins
        if resource_available(user_response)==True:
            print('Enter Your Coins.....')
            user_penny=int(input('Enter Penny: '))
            user_nickel=int(input('Enter Nickel: '))
            user_dime=int(input('Enter Dime: '))
            user_quarter=int(input('Enter Quarter: '))
            
            coins_total=coins['penny']*user_penny+coins['dime']*user_dime+\
            coins['nickel']*user_nickel+coins['quarter']*user_quarter
            
            # check whwther enough coins
            if enough_coins(user_response,coins_total):
                print(f'We are preparing  {user_response} for you...')
                deduct_resources(user_response)
                change,total_amount=deduct_money(user_response,coins_total,total_amount) # deduct money save change and total amount in account
                #print bill
                print_bill()
            else:
                print('Sorry Not Enough Coins')

        else:
            print('Sorry Resources Not Available')
    else:
        print('Enter Valid Name....  ')  




#3 both available make coffe else sorry


