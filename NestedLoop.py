for x in range(2):
    for y in range(0,3):
        print(y)
    

for x in range(3):
    for y in range(0,10):
        print(y)

y = int(input("Enter The Number:"))
for x in range(y):
    for z in range(0,y):
        print(z)


rown = int(input("Enter The Number of Rows:"))
coloumn = int(input("Enter The Number of Columns:"))
symbol = "*"
for x in range(rown):
    for y in range(coloumn):
        print(symbol, end=" ")
    print()