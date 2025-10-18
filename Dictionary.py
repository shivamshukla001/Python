# dictionary = a collection of key-value pairs pairs ordered and changeable. No duplicate members.
# used to store data values like a map, which unlike other Data Types that hold only single values as an element.

# Methods
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs

menu = {
    "burger": 8.99,
    "fries": 3.49,
    "drink": 1.99,
    "momos": 5.99
    }

cart = []
total= 0

for key,values in menu.items():
    print(f"{key}: ${values}")

while True:
    food = input("What would you like to order? (type 'quit' to finish): ").lower()

    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
        print("--------- YOUR oRDER---------")

        for food in cart:
          
            total += menu.get(food)
            print(f"{food}: ${menu.get(food)}")
        print(f"Total: ${total:.2f}")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")


