def count_vowels(text):
    if text == "":
        return 0
    if text[0].lower() in "aeiou":
        return 1 + count_vowels(text[1:])
    else:
        return 0 + count_vowels(text[1:])
print(count_vowels("I love python"))