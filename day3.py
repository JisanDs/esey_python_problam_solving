#🏆 Day 3 Problem Solving Pack



"""🔶 Problem 1: Sum Without Highest and Lowest

Problem:
Write a function that takes a list of numbers, removes the highest and lowest value, and returns the sum of the remaining numbers.

Example:

sum_middle([6, 2, 1, 8, 10]) ➔ 16  (because 6+2+8 = 16 after removing 1 and 10)
sum_middle([1, 1, 11, 2, 3]) ➔ 6  (because 2+3+1 = 6 after removing 1 and 11)"""

lst = [6, 2, 1, 8, 10]

def sum_middle(lst):
    small = lst[0]
    gt = lst[0]
    for i in range(1, len(lst)):
        if lst[i] <= small:
            sm = lst[i]
        elif lst[i] >= gt:
            gt = lst[i]

    lst.remove(sm)
    lst.remove(gt)

    return sum(lst)

print(sum_middle([6, 2, 1, 8, 10]))
print(sum_middle([1, 1, 11, 2, 3]))
print(sum_middle([6, 2, 1, 1, 8, 11, 11, 10]))

"""🔶 Problem 2: Count of Positives / Sum of Negatives

Problem:
Given an array of integers, return an array where:
The first element is the count of positive numbers.
The second element is the sum of negative numbers.


Example:

count_sum([1, 2, 3, -4, -5]) ➔ [3, -9]
count_sum([0, -1, -2]) ➔ [0, -3]"""

def count_sum(lst):
    if not lst:
        return []

    count_p = sum(1 for num in lst if num > 0)
    sum_n = sum(num for num in lst if num < 0)
    return [count_p, sum_n]

print(count_sum([1, 2, 3, -4, -5]))
print(count_sum([0, -4, -5]))
print(count_sum([]))

"""🔶 Problem 3: Vowel Count

Problem:
Write a function that returns the number of vowels (a, e, i, o, u) in a given string.

Example:

vowel_count("hello") ➔ 2
vowel_count("beautiful") ➔ 5"""

def vowel_count(s):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
    return vowel_count
    
print(vowel_count("hello"))
print(vowel_count("beautiful"))


"""🔶 Problem 4 (Bonus Easy): Is the String Uppercase?

Problem:
Write a function that returns True if the entire string is uppercase, otherwise False.

Example:

is_upper("HELLO") ➔ True
is_upper("Hello") ➔ False"""


def is_upper(name):
    return name == name.upper()

print(is_upper("Jisan"))
print(is_upper("JISAN"))

print(is_upper("HELLO"))
print(is_upper("Hello"))