
# formule: x if comdition else y
a = 10
b = 20
min_value = a if a>b else b
# print(min_value)  # Output: 20

user_role="guest"
acces = "full Acess" if user_role=="admin"else "Limited Access"
# print(acces)  # Output: full Acess

age = 22
is_adult = "adult" if age > 18 else "notAdult"
# print(is_adult)  # Output: adult

num = 3
parity = "even" if num % 2==0 else "odd"
# print(parity)

num=51521
divisible = "divisible by 5" if num%5==0 else "not divisible by 5"
print(divisible)
