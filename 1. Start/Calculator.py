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


print(sum(1,2))
print(divide(5,0))