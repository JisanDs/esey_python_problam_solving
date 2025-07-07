"""🏁 Day 9 – Problem Solving Pack

Focus:
🔹 List & String Manipulation
🔹 Logical Thinking
🔹 Loops + Conditionals"""



"""✅ 🔶 Problem 1: Filter Even Numbers

Problem:
Write a function that takes a list of numbers and returns a new list with only the even numbers.

Example:

filter_even([1, 2, 3, 4, 5, 6]) ➞ [2, 4, 6]  
filter_even([10, 13, 15, 20]) ➞ [10, 20]"""


"""def filter_even(lst):
    even = []
    for n in lst:
        if n % 2 == 0:
            even.append(n)
    return even

lst = [1, 2, 3, 4, 5, 6]

print(filter_even(lst))
print(filter_even([10, 13, 15, 20]))
print(filter_even([101, 613, 715, 820]))"""


"""✅ 🔶 Problem 2: Capitalize First Letter of Each Word

Problem:
Write a function that takes a sentence and returns it with the first letter of each word capitalized.

Example:

capitalize_words("hello world") ➞ "Hello World"  
capitalize_words("python is fun") ➞ "Python Is Fun"""


def capitalize_words(word):
    w_split = word.split(" ")
    capital = " ".join(w.capitalize() for w in w_split)
    return capital
    
print(capitalize_words("hi my name is jisan"))
print(capitalize_words("hello world"))
print(capitalize_words("python is fun"))
print(capitalize_words("sonnic very very thenks"))