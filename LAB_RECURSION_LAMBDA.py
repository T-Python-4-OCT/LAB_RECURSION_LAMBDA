# Task 1: Recursion

def count_vowels(text):

    # Base case
    if text == "":
        return 0

    # Check first letter
    if text[0].lower() in "aeiou":
        return 1 + count_vowels(text[1:])
    else:
        return count_vowels(text[1:])


phrase = "I love python"
print("Task 1:")
print("Number of vowels:", count_vowels(phrase))


# Task 2: map() and lambda
numbers = [40, 35, 10, 15, 20]

list = list(map(lambda x: x * x, numbers))

print("\nTask 2:")
print("New list:", list)


# -----output------
 # Task 1:
# Number of vowels: 4

# Task 2:
# New list: [1600, 1225, 100, 225, 400] 