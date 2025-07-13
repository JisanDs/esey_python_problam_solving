"""🏁 Day 10 – Problem Solving Pack
🔹 Focus:

🔶 Nested Logic
🔶 Conditions + Loops
🔶 Small Math Patterns"""



"""✅ 🔶 Problem 1: Find the Factorial

Problem:
Write a function that takes a number and returns its factorial.
(Use loop, not recursion)

📌 Example:

factorial(5) ➞ 120   # 5×4×3×2×1  
factorial(1) ➞ 1  
factorial(0) ➞ 1"""

"""def factorial(n):
    fact = 1
    for n in range(n, 0, -1):
        fact *= n
    return fact

print(factorial(5))
print(factorial(1))
print(factorial(0))
print(factorial(12))"""

"""✅ 🔶 Problem 2: Count Words in a Sentence

Problem:
Write a function that counts how many words are in a sentence.

📌 Example:

count_words("I love programming") ➞ 3  
count_words("Python is powerful") ➞ 3  
count_words("Hello") ➞ 1

👉 Hint: Use .split() method."""

"""def count_words(s):
    split_s = s.split(" ")
    return len(split_s)
    
print(count_words("I love programming"))
print(count_words("Python is powerful"))
print(count_words("Hello"))
print(count_words("This is what problam solving feels like"))"""


"""🔶 Problem 3: FizzBuzz

Problem: Write a function that prints numbers from 1 to n.

For multiples of 3, print "Fizz" instead of the number.

For multiples of 5, print "Buzz".

For numbers that are multiples of both 3 and 5, print "FizzBuzz".


📌 Example:

fizzbuzz(15)
# Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz"""

"""def fizzbuzz(n):
    for n in range(1, n+1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

fizzbuzz(15)
fizzbuzz(20)"""


"""🔶 Problem 4: Sum of Squares

Problem: Write a function that returns the sum of squares of all numbers from 1 to n.

📌 Example:

sum_of_squares(3) ➞ 14  # 1² + 2² + 3² = 14  
sum_of_squares(5) ➞ 55"""


"""def sum_of_squares(n):
    sum = 0
    for s in range(1, n+1):
        sum += s**2
    return sum

print(sum_of_squares(3))
print(sum_of_squares(5))"""