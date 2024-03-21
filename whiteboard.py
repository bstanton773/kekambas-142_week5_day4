# The Hamming Distance is a measure of similarity between two strings of equal length. Complete the function so that it returns the number of differences between the two strings.

# Examples:
# a = "I like turtles"
# b = "I like turkeys"
# Result: 3

# a = "Hello World"
# b = "Hello World"
# Result: 0

#a = "espresso"
#b = "Expresso"
# Result: 2

# Notes:
# You can assume that the two inputs strings of equal length.

def solution(string1, string2):
    differences = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            differences += 1
    return differences

def solution(s1,s2):
    differences = 0
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            differences += 1
    return differences

def solution(s1, s2):
    diff = 0
    for idx, val in enumerate(s1):
        if s1[idx] != s2[idx]:
            diff += 1
    return diff
