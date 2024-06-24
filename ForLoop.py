from array import *

numbers = array("i",[])

n = int(input("Enter the lenth of the array: "))

for i in range(n):
    x = int(input("Enter the next number: "))
    numbers.append(x)

print(numbers)

#We want the user to request the index of a number in the array

num = int(input("Please enter the number: "))

count = 0
for f in numbers:
    if f == num:
        break
    count = count + 1

print(f"The index of the number is ", count)
