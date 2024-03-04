# Nested loop = loop within loop
row=int(input("Enter how many row you want to print ?"))
coloumn=int(input("Enter how many coloumn you want to print ?"))
symbol=input("Which symbol you want to use ?")

for i in range(row):
    for j in range(coloumn):
        print(symbol,end="")
    print()