#1
"""def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(8))"""
#2
"""def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vivod = ""
    for char in string:
        if char not in vowels:
            vivod += char

    return vivod

print(remove_vowels("apple"))
print(remove_vowels("orange"))
print(remove_vowels("pear"))
print(remove_vowels("pineapple"))
print(remove_vowels("durian"))
print(remove_vowels("banana"))"""

#3
def pascal_recursive(n, triangle = None):
    if triangle is None:
        triangle = [[1]]

    if len(triangle) == n:
        return triangle

    last_row = triangle[-1]
    new_row = [1]
    for i in range(1, len(last_row)):
        new_row.append(last_row[i - 1] + last_row[i])
    new_row.append(1)
    triangle.append(new_row)

    return pascal_recursive(n, triangle)

n = 8
triangle = pascal_recursive(n)

print(f'Треугольник Паскаля для n = {n}:')
for row in triangle:
    print(row)