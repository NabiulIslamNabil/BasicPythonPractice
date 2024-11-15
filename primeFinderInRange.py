# Print all prime numbers within a range
# start = 25
# end = 50
# Expected output:
# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47
from math import sqrt

def primeFinder(num):
    flag = True
    for i in range (2, int(sqrt(num)+1)):
        if num%i==0:
            flag = False
            break
    if flag and num != 1:
        return True
    else:
        return False  


starting = int(input("Enter the start value: "))
ending = int(input("Enter the ending value: "))
print("Prime numbers in the range", starting, "to", ending, "are: ")
for i in range(starting, ending+1):
    if primeFinder(i):
        print(i)
