# Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# Expected output:
# 50
# 40
# 30
# 20
# 10
myList = [10, 20, 30, 40, 50]
n = len(myList)
for i in range(n-1, -1, -1):
    print(myList[i])