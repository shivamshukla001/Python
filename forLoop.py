#  execute a block of code a fixed number of times
# you can iterate over a sequence (like a list, tuple, or string) or use the range() function to generate a sequence of numbers.

for x in reversed(range(1,11,3)):
    print(x)
print("Happy New Year!" )

creditcard="1234-5678-9101-1121"

for x in creditcard:
    if x == "-":
        continue
    print(x)


for x in range(1,21):
    if x==13:
        print("Unlucky 13!")
        continue
    print(x)

for x in range(12,35):
    if x%2 == 0:
        print(x)


