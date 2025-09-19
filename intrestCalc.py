principle = 0
time=0
rate=0
while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("Principle amount must be greater than 0. Please try again.")

while rate <=0:
    rate = int(input("Enter the intrest rate: "))
    if rate<=0:
        print("Intrest can not be zero or less")
    
while time <=0:
    time = int(input("Enter the time in years: "))
    if(time<=0):
        print("Time can not be zero or less")

total = principle * pow((1+rate/100),time)

print(f"The total amount after {time} years is {total:.2f}")