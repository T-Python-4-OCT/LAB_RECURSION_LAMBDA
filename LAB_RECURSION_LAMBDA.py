def count_vowels(phrase: str) -> int:
    if not phrase:
        return 0

    current_is_vowel = phrase[0].lower() in "aeiou"
    return int(current_is_vowel) + count_vowels(phrase[1:])


print(count_vowels("I love python"))

numbers = [40, 35, 10, 15, 20]
squared_numbers = list(map(lambda number: number * number, numbers))
print(squared_numbers)