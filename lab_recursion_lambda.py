def count_vowels(text):
    if text == "":
        return 0
    if text[0].lower() in "aeiou":
        return 1 + count_vowels(text[1:])
    return count_vowels(text[1:])


print(count_vowels("hi i am learning python and it is fun"))



print("="*40)

numbers = [40, 35, 10, 15, 20]
squares = list(map(lambda n: n * n, numbers))
print(squares)