def count_vowels(text):
    if not text:
        return 0

    first_count = 1 if text[0].lower() in "aeiou" else 0
    return first_count + count_vowels(text[1:])


print(count_vowels("I love python"))

numbers = [40, 35, 10, 15, 20]
squared_numbers = list(map(lambda number: number * number, numbers))
print(squared_numbers)
