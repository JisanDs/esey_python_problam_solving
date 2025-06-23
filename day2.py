#🏆 Day 2 Problem Solving Pack:



"""🔶 Problem 1: Reversed Strings

Problem:

Complete the function that takes a string and returns the reversed version of it.

Example:

reverse_string("hello") ➔ "olleh"
reverse_string("world") ➔ "dlrow"""

"""def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1 : len(s)]) + s[0]
    
print(reverse_string("sonnic"))
print(reverse_string("hello"))
print(reverse_string("world"))"""

"""🔶 Problem 2: Sum of Positive

Problem:

You will be given an array of numbers. Return the sum of all positive numbers.

Example:

sum_of_positive([1, -4, 7, 12]) ➔ 20
sum_of_positive([-1, -2, -3]) ➔ 0"""

"""def sum_of_positive(lst):
    if sum(lst) <= 0:
        return 0
    else:
        sum_lst = []
        for i in lst:
            if i < 0:
                continue
            else:
                sum_lst.append(i)
        return sum(sum_lst)
    
print(sum_of_positive([1, -4, 7, 12]))
print(sum_of_positive([-1, -2, -3]))
print(sum_of_positive([1, -4, 7]))"""


"""🔶 Problem 3: String Repeat

Problem:

Write a function that takes a string and a number n, and returns the string repeated n times.

Example:

repeat_string("abc", 3) ➔ "abcabcabc"
repeat_string("xyz", 0) ➔ "" """

"""def repeat_string(s, n):
    rep = ""
    for i in range(n):
        rep += s
    return rep
    
print(repeat_string("abc", 3))
print(repeat_string("abc", 0))"""


"""🔶 Problem 4 (Bonus Easy): Double Char

Problem:

Write a function that takes a string and returns a string where each character is repeated once.

Example:

double_char("abc") ➔ "aabbcc"
double_char("123") ➔ "112233"""

"""def double_char(word):
    n_word = ""
    for i in word:
        n_word += i+i
    return n_word
        
print(double_char("abc"))
print(double_char("123"))
print(double_char("sonnic"))"""