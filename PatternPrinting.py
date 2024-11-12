# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

n = int(input("Enter how many lines: "))

for i in range(1, n+1):
    j = 1
    while (j<=i):
        print(j, end=' ')
        j+=1
    print("")