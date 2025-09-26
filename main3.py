num = input("Enter the number:")

if len(num)>=4:
    mid = len(num)//2
    midOne = int(num[mid])
    midTwo = int(num[mid-1])

    product = midOne * midTwo
    print(product)
else:
    print("It is not more than or equal to 4 digits")