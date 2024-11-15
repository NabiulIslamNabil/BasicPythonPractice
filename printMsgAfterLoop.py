# Display a message “Done” after the successful execution of the for loop
# Expected output:
# 0
# 1
# 2
# 3
# 4
# Done!

n = int(input("Enter the number of rows: "))
msg = input("Enter the message: ")
for i in range(0, n):
    if not i == n:
        print(i)
    
print(msg)
