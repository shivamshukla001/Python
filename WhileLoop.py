
name = input("Enter Your Name: ")

while name == "":
    print("Name cannot be empty. Please enter your name.")
    name = input("Enter Your Name: ")
print(f"Welcome {name}")

age = int(input("enter Your Age: "))

while age < 0 :
    print("Age must be between 0 and 120. Please enter a valid age.")
    age = int(input("enter Your Age: "))
print(f"Your age is {age}")


food = input("Enter Your Favourite Food(press q to exit): ")

while not food=='q':
    print(f"Your Favourite Food is {food}")
    food = input("Enter Your Favourite Food(press q to exit): ")
print("bYE bHOSDI.")

num = int(input("Enter a number between 1 to 10: "))

while num < 1 or num > 10:
    print("Number must be between 1 and 10. Please try again.")
    num = int(input("Enter a number between 1 to 10: "))
print(f"You entered {num}. Thank you!")