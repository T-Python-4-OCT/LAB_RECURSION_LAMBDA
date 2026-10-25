def count_vowels(text):
    if not text:
        return 0
    return (text[0].lower() in "aeiou") + count_vowels(text[1:])


print(count_vowels("I love github"))  