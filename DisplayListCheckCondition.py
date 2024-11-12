# Write a Python program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

myList = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    e = int(input("Enter the element(integer): "))
    myList.append(e)

for ele in myList:
    if(ele > 500):
        break
    if(ele>150):
        continue
    if(ele%5==0):
        print(ele)


#inputs
# 7 12 75 150 180 145 525 50