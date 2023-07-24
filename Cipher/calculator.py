a=2
b=5

def add(a,b):
    return a+b

def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
symbols={
    '+':add(a,b),
    '-':sub(a,b),
    '*':multiply,
    '/':divide,
}

def calculator(symbol):
    return symbols[symbol]
print(calculator('+'))