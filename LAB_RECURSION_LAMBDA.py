# 1)
def count_vowels(text):
    if text == "":
        return 0
    first = 1 if text[0].lower() in "aeiou" else 0
    return first + count_vowels(text[1:])


print(count_vowels("I love python"))  # 4


# 2) 
numbers = [40, 35, 10, 15, 20]
squared = list(map(lambda n: n * n, numbers))
print(squared)  # [1600, 1225, 100, 225, 400]
