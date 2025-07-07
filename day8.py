"""🏁 Day 8 – Problem Solving Pack
🔹 String formatting
🔹 Basic math logic
🔹 Conditionals"""


"""✅ 🔶 Problem 1: Format Phone Number

Problem:
Write a function that takes a list of 10 integers (0–9) and returns them as a formatted phone number string like (123) 456-7890.

Example:

format_phone([1,2,3,4,5,6,7,8,9,0]) ➞ "(123) 456-7890"""

def format_phone(numbers):
    if len(numbers) != 10:
        return "This numbers is invalid"
    else:
        area = "".join(str(i) for i in numbers[0:3])
        middle = "".join(str(i) for i in numbers[3:6])
        last = "".join(str(i) for i in numbers[6:10])
        return f"({area}) {middle}-{last}"
        
print(format_phone([8,8,8,4,5,6,7,8,9,9]))
print(format_phone([1,2,3,4,5,6,7,8,9]))
print(format_phone([1,2,3,4,5,6,7,8,9,0]))
print(format_phone([8,8,8,4,5,6,7,8,9,9,3]))

"""✅ 🔶 Problem 2: Make a List of Multiples

Problem:
Write a function that returns a list of the first n multiples of a given number x.

Example:

multiples(3, 5) ➞ [3, 6, 9, 12, 15]  
multiples(2, 4) ➞ [2, 4, 6, 8]"""


def multiples(n, x):
    mul = []
    for m in range(1, x+1):
        ml = m * n
        mul.append(ml)
    return mul
    
print(multiples(3, 5))
print(multiples(2, 4))
print(multiples(15, 10))