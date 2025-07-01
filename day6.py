#✅ 🏆 Day 6 – Problem Solving Pack



"""🔶 Problem 1: Find the Odd Integer

Problem:
Given an array of integers where all values appear an even number of times except one, return the integer that appears an odd number of times.

Example:

find_odd([20, 1, 1, 2, 2, 3, 3]) ➞ 20  
find_odd([10, 10, 10, 10, 11]) ➞ 11  
find_odd([5, 5, 5, 4, 4]) ➞ 5"""


def find_odd(lst):
    checked = []
    count = 0
    for n in lst:
        if n not in checked:
            count = lst.count(n)
            if count % 2 != 0:
                return n
            checked.append(n)

lst =[3, 4, 4, 5, 5, 20, 20, 7, 7, 7]
print(find_odd(lst))
print(find_odd([20, 1, 1, 2, 2, 3, 3]))
print(find_odd([10, 10, 10, 10, 11]))
print(find_odd([5, 5, 5, 3, 3]))

print("Print function :")
#print function
def find_odd(lst):
    checked = []
    count = 0

    for n in lst:
        if n not in checked:
            count = lst.count(n)
            if count % 2 != 0:
                print(n)
            checked.append(n)

lst =[3, 4, 4, 5, 5, 20, 20, 7, 7, 7]
find_odd(lst)
find_odd([20, 1, 1, 2, 2, 3, 3])
find_odd([10, 10, 10, 10, 11])
find_odd([5, 5, 5, 4, 4])

"""🔶 Problem 2: Age Difference

Problem:
You are given a list of integers representing ages. Return the difference between the oldest and youngest person (i.e., max(age) - min(age)).

Example:

age_diff([10, 15, 20, 25]) ➞ 15  
age_diff([100, 50]) ➞ 50  
age_diff([1, 1, 1]) ➞ 0"""


def age_diff(lst):
    max = lst[0]
    mini = lst[0]
    for i in range(1, len(lst)):
        if max < lst[i]:
            max = lst[i]
        elif mini > lst[i]:
            mini = lst[i]
    return max - mini
    
print(age_diff([10, 15, 20, 25]))
print(age_diff([100, 50]))
print(age_diff([1, 1, 1]))
print(age_diff([99, 78, 87, 4]))