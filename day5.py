"""✅ 🏆 Day 5 – Problem 1: Reverse Words in a Sentence (Easy)

🔸 Problem:
Write a function that takes a sentence (string) and returns the sentence with the order of the words reversed.

🔹 Example:

reverse_words("Hello world") ➞ "world Hello"
reverse_words("Python is fun") ➞ "fun is Python"
reverse_words("I love coding") ➞ "coding love I"""

s = "Hello world"

def reverse_words(s):
    split_word = s.split()
    rev_spl_word = split_word[ : :-1]
    new_str = " ".join(rev_spl_word)
    return new_str

print(reverse_words("Hello world"))
print(reverse_words("Python is fun"))
print(reverse_words("I love coding"))