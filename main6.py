#take input from the user
rowsize = int(input("Enter the number of rows"))
if rowsize%2==0:
    halfdaim=int(rowsize/2)
else:
    halfdaim=int(rowsize/2)+1

space = halfdaim -1

#loop for upperpart
for i in range(1,halfdaim+1):
    for j in range(1, space+1):
        print(end=" ")
    space = space - 1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        #increasing number on each column
        num = num + 1
    print()
space = 1

#loop for lower part
for i in range(1,halfdaim):
    for j in range(1, space+1):
        print(end=" ")
    space = space + 1
    num = 1
    for j in range(1, 2*(halfdaim-i)):
        print(end=str(num))
        num = num + 1
    print()