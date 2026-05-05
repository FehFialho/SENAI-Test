def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if (b == 0):
        print("Can't divide by 0!")
        return
    return a / b

def multiply(a, b):
    return a * b

def lowerValue(a,b):
    if (a == b):
        return a
    if (a>b):
        return b
    return a

def evenOdd(x):
    if (x % 2 == 0):
        return "even"
    return "odd"