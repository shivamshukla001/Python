username = input("Enter your username: ")



if len(username)>12:
    print("Username must be at most 12 characters long.")
elif not username.find( " ")== -1:
    print("Username must not contain spaces.")
elif not username.isalpha():
    print("Username must contain only alphabetic characters not numbers.")
else: 
    print(f"welcome {username}")