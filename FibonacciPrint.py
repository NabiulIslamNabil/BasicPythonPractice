# Display Fibonacci series up to n terms
# Expected input: 10
# Expected output:
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
myList = []

def fibonacciFinder(first, last, num):
    if(len(myList)==10):
        return
    else:
        myList.append(first)
        fibonacciFinder(last, first+last, num)


n = int(input("Enter the number: "))
fibonacciFinder(0, 1, n)
for i in range(0, n):
    print(myList[i], end=" ")