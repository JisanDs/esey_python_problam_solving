#🏁Day 7 – Problem Solving

#🔹 String manipulation
#🔹 Number logic with conditionals



"""✅ 🔶 Problem 1: Remove First and Last Character

Problem:
Write a function that removes the first and last characters from a string. If the string has less than 2 characters, return an empty string.

Example:

remove_ends("hello") ➞ "ell"  
remove_ends("a") ➞ ""  
remove_ends("ab") ➞ """

"""def remove_ends(s):
    return s[1:-1]

print(remove_ends('sinnic'))
print(remove_ends("hello"))
print(remove_ends("a"))
print(remove_ends("ab"))"""

"""✅ 🔶 Problem 2: Abbreviate a Name

Problem:
Write a function that takes a two-word name and returns the initials in uppercase separated by a dot.

Example:

abbrev_name("john doe") ➞ "J.D"  
abbrev_name("mary jane") ➞ "M.J"""

def abbrev_name(s):
    split_s = s.split(" ")
    char1 = split_s[0][0]
    char2 = split_s[1][0]
    join = char1 + "." + char2
    return join.upper()
    
print(abbrev_name("jisan sonnic"))
print(abbrev_name("john doe"))
print(abbrev_name("mary jane"))

#sort version

def abbrev_name1(s):
    return '.'.join([word[0] for word in s.split()]).upper()
    
print(abbrev_name1("jason statham"))