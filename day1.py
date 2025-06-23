#🏆 Day 1 Problem Solving Pack:



"""🔶 Problem 1: Return Negative

Problem:
Write a function that takes a number. If the number is positive, return it as negative. If it's already negative or zero, return it as is.

Example:

make_negative(7) ➔ -7
make_negative(-4) ➔ -4
make_negative(0) ➔ 0"""

"""def make_negative(num):
    if num == 0:
        return num
    elif num < 0:
        return num
    else:
        return -num

print(make_negative(7))
print(make_negative(-4))
print(make_negative(0))"""


"""🔶 Problem 2: Opposites Attract

Problem:
If one person is even and the other is odd, they are in love.
Write a function that takes two numbers and returns True if one is even and the other is odd, otherwise False.

Example:

lovefunc(2, 3) ➔ True
lovefunc(4, 4) ➔ False
lovefunc(7, 10) ➔ True"""

"""def lovefunc(num1, num2):
    return (num1 % 2 == 0) != (num2 % 2 == 0)
    
print(lovefunc(2, 3))
print(lovefunc(4, 4))
print(lovefunc(7, 10))"""


"""🔶 Problem 3: First Non-Consecutive Number

Problem:
Given a list of numbers, return the first non-consecutive number. If all numbers are consecutive, return None.

Example:

first_non_consecutive([1, 2, 3, 4, 6]) ➔ 6
first_non_consecutive([4, 5, 6, 7, 8]) ➔ None"""

"""def first_non_consecutive(lst):
    if len(lst) <= 1:
        return lst
    else:
        for i in range(1, len(lst)):
            if lst[i] != lst[i-1] + 1:
                return lst[i]
        return None
            
print(first_non_consecutive([1, 2, 3, 4, 6]))"""


"""🔶 Problem 4 (Bonus Easy): Are You Playing Banjo?

Problem:
If a name starts with "R" or "r", return:
"name plays banjo"
Otherwise:
"name does not play banjo"

Example:

are_you_playing_banjo("Rick") ➔ "Rick plays banjo"
are_you_playing_banjo("John") ➔ "John does not play banjo"""


def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return (f"{name} plays banjo")
    else:
        return (f"{name} dose not play banjo")
        
print(are_you_playing_banjo("Rick"))
print(are_you_playing_banjo("John"))