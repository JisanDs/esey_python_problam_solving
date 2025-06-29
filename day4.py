#✅ 🏆 Day 4: Problem Solving Pack (Math/Logic Focused – Only 2 Problems)

"""🔶 Problem 1: Find the Next Perfect Square

Problem: Write a function that takes a number and returns the next perfect square.
If the number is not a perfect square, return -1.

Example:

next_perfect_square(121) ➞ 144  
next_perfect_square(625) ➞ 676  
next_perfect_square(114) ➞ -1"""

def next_perfect_square(num):
    root = num ** 0.5
    if root == int(root):
        return (int(root) + 1) ** 2
    else:
        return -1

print(next_perfect_square(121))
print(next_perfect_square(625))
print(next_perfect_square(114))
print(next_perfect_square(9))

"""🔶 Problem 2: Sum of Digits Until Single Digit

Problem: Write a function that takes a number and adds its digits repeatedly until the result is a single digit.

Example:

single_digit_sum(942) ➞ 6  # 9+4+2=15 ➞ 1+5=6  
single_digit_sum(132189) ➞ 6  
single_digit_sum(9) ➞ 9"""

# for loop with recursion
"""def single_digit_sum(digits):
    sum_digits = 0
    for num in str(digits):
        sum_digits += int(num)
    return (sum_digits // 10) + (sum_digits % 10)
    
    
print(single_digit_sum(942))
print(single_digit_sum(132189))
print(single_digit_sum(9))
print(single_digit_sum(992))"""

# while loop and for loop

def single_digit_sum(digits):
    while digits >= 10:
        sum_digits = 0
        for num in str(digits):
            sum_digits += int(num)
        digits = sum_digits
    return digits
    
print(single_digit_sum(942))
print(single_digit_sum(132189))
print(single_digit_sum(9))
print(single_digit_sum(992))