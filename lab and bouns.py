def count_vowels(text):
    if text == "":
        return 0

    if text[0].lower() in "aeiou":
        return 1 + count_vowels(text[1:])
    else:
        return count_vowels(text[1:])


phrase = input("Enter a word or phrase: ")
print(count_vowels(phrase))
print("*" * 20)

numbers = [40, 35, 10, 15, 20]

new_numbers = list(map(lambda number: number * number, numbers))

print(new_numbers)