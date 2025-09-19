unit = input("Enter the unit you want to convert to (C/F): ").upper()
temp = float(input("Enter the temperature you want to convert: "))

if unit == "C":
    temp = round(9*temp/5 + 32,1)
    print(f"The temperature in Fahrenheit is {temp} F")
elif unit =="F":
     round((temp-32)*5/9,1)
     print(f"The temperature in Celsius is {temp} C")
else:
    print("Please enter a valid unit (C/F)")