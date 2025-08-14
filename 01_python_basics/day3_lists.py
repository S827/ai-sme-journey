"""
Basic Access & Modify

Create a list of 5 fruits

Replace the second fruit with "dragonfruit"

Append a new fruit "papaya"

Remove the first fruit
"""
fruits = ['apple', 'banana', 'kiwi', 'orange', 'mango']
print(fruits)
fruits[1] = 'dragonfruit'
print(fruits)
fruits.append('papaya')
print(fruits)
del fruits[0]
print(fruits)

"""
List Comprehension

From a list of numbers 1–20, create:

A list of squares of even numbers

A list of numbers divisible by 3
"""
num = list(range(1, 21))
print(num)

squares_of_even = [n**2 for n in num if n % 2 == 0]
print(squares_of_even)

num_div_3 = [n for n in num if n % 3 == 0]
print(num_div_3)

"""
Nested List Access

Given:

python
Copy
Edit
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
Print the value 80

Change 60 to 100
"""
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(matrix[2][1])
matrix[1][2] = 100
print(matrix)

"""
Sorting

Sort a list of names alphabetically and in reverse order.
"""
names = ['div', 'eto', 'ali', 'sia', 'toni', 'jay']
print(sorted(names))
# print(names)
names.sort(reverse=True)
print(names)