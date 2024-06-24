import array

from numpy import *
from array import *
import random

#print(42*60+42)
#distance = 10/1.61
#print("The number of miles in 10 kilometers is",distance)

# 1 km = 1000 m
# speed = distance/time
#time = 42*60+42
#speed = distance/time
#print("The average speed is",speed,"miles per second")

#numbers = array([3,4,5,7,8])
#print(numbers.max())

#names = array(["James","Ken","Pato","Jack"])
#print(names[2])


#to create a function, we use the def key-word, followed by the name.
#Create a function that takes two values and find their sum.


"""
def sum(a,b):
    return a+b

print(sum(3,4))

def average(a,b,c,d):
    return (a+b+c+d)/4

print(average(3,6,7,8))
"""

number = random.randint(0,100)

while True:
    user = int(input("Guess a number: "))
    if user < number:
        print("Lower")
    elif user > number:
        print("Higher")
    elif user == number:
        print("Congratulation, you won")
        break

