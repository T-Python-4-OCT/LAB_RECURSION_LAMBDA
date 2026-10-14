def count_vowels(text):
    if text == "":
        return 0

    if text[0].lower() in "aeiou":
        return 1 + count_vowels(text[1:])

    return count_vowels(text[1:])

print("--------Question 1-------")
print(count_vowels("I love python"))   
print("")
print("--------Question 2-------")
numbers = [40, 35, 10, 15, 20]
squared = list(map(lambda n: n * n, numbers))
print(squared)   