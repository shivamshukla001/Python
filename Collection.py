Collection = single variable use to store multiple values
List = [] ordered unchangeable, allow duplicate values
Dictionary = {} unordered, changeable, indexed, no duplicate keys
set = {} unordered, unindexed, no duplicate values
Tuple = () ordered, unchangeable, allow duplicate values

# -----------------------List-----------------------


list=["apple", "banana", "cherry"]
print(list[1])  # Output: banana
print(list[:2])  # Output: ['apple', 'banana']
print(list[-1])  # Output: cherry

for x in list:
    print(x)

for x in list:

    if x =="banana":
        print(x)
        break
    else:
        print("not found")

-----------------------Important Methods-----------------------
print(dir(list))  # Output: List of all attributes and methods of list object

# print(len(list))  # Output: 3

print(list.append("orange"))  # Output: None (appends orange to the end of the list)
print(list)  # Output: ['apple', 'banana', 'cherry', 'orange']

print(list[3])

print(list.insert(1, "kiwi"))  # Output: None (inserts kiwi at index 1)
print(list)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']

print(list.remove("banana"))  # Output: None (removes banana from the list)
print(list)  # Output: ['apple', 'kiwi', 'cherry', 'orange']

print(list.pop())  # Output: orange (removes and returns the last item)
print(list)  # Output: ['apple', 'kiwi', 'cherry']
print(list.reverse())  # Output: None (reverses the list   )
print(list)  # Output: ['cherry', 'kiwi', 'apple']

print(list.sort())  # Output: None (sorts the list in ascending order)
print(list)  # Output: ['apple', 'cherry', 'kiwi']

print(list.index("cherry"))  # Output: 2 (returns the index of cherry)
print(list.count("apple"))  # Output: 1 (returns the count of kiwi in the list)


# -----------------------SETS-----------------------


myset = {"apple", "banana", "cherry"}
print(myset)  # Output: {'banana', 'cherry', 'apple'}
print(type(myset))  # Output: <class 'set'>
add = myset.add("orange")  # Output: None (adds orange to the set)
print(myset)  # Output: {'banana', 'cherry', 'orange', 'apple'}

myset.add("orange")
print(myset)  # Output: {'banana', 'cherry', 'orange', 'apple'}
print(len(myset))  # Output: 4
myset.remove("banana")  # Output: None (removes banana from the set)
print(myset)  # Output: {'cherry', 'orange', 'apple'}
myset.discard("cherry")  # Output: None (removes cherry from the set)
print(myset)  # Output: {'orange', 'apple'}
myset.pop()  # Output: apple (removes and returns an arbitrary item)
print(myset)  # Output: {'orange'}
myset.clear()  # Output: None (removes all items from the set)
print(myset)  # Output: set()

# -----------------------Tuple-----------------------
mytuple = ("apple", "banana", "cherry")
print(mytuple)  # Output: ('apple', 'banana', 'cherry')
print(type(mytuple))  # Output: <class 'tuple'>
print(mytuple[1])  # Output: banana
print(mytuple[-1])  # Output: cherry
for x in mytuple:
    print(x)    


