# list comprehension a concise way to create lists compact and easier to read then traditional loops


                            # ------Formula------
# [expression for item in iterable if condition]
#  --------------------------------------------------------------------------

double = [x*2 for x in range(0,10)]
# print(double)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

triple = [item * 3 for item in range(0,11)]
# print(triple)  # Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits = [ fruit.upper() for fruit in fruits]
# print(fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

numbers = [-1, 3, 5, -2, 0, 8, -7, 4]
positive_nums = [num for num in numbers if num >=0]
# print(positive_nums)  # Output: [3, 5, 0, 8, 4]

negative_nums = [num for num in numbers if num < 0 ]
# print(negative_nums)  # Output: [-1, -2, -7]

even_number = [ num for num in numbers if num % 2 == 0]
# print(even_number)  # Output: [ -2, 0, 8]

odd_number = [num for num in numbers if num % 2 == 1]
# print(odd_number)  # Output: [3, 5, -7, -1]

multiple_of_two = [ num*2 for num in numbers if num]
# print(multiple_of_two)  # Output: [-2, 6, 10, -4, 0, 16, -14, 8]

grades = [65, 70, 75, 80, 85, 90, 95]
passing_grade = [ grade for grade in grades if grade >=85]
# print(passing_grade)  # Output: [65, 70, 75, 80, 85, 90, 95]

fail_grade = [ grade for grade in grades if grade <=70]
# print(fail_grade)  # Output: [65, 70]



    

