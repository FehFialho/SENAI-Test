import math

def square(a, b):
    return a * b

def triangle(b,h): # basis * heigth
    return b * h / 2

def elipsis(a,b):
    return round((a * b * math.pi), 2)

#print(elipsis(6,5))