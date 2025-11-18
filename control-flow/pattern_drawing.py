size = int(input('Enter the size of the pattern: '))
rowcount = 0
while rowcount < size:
    for i in range(size):
        print("*", end="")
    print()
        #i = i + 1
    rowcount = rowcount + 1