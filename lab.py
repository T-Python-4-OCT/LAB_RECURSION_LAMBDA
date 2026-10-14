def count_vowels(phrase):

    if phrase == "":
        return 0

    first_letter = phrase[0].lower()

    if first_letter in "aeiou":
        return 1 + count_vowels(phrase[1:])

    return count_vowels(phrase[1:])


print(f"Part 1 - Number of vowels: {count_vowels('I love python')}")


numbers = [40, 35, 10, 15, 20]

squared_numbers = list(map(lambda number: number * number, numbers))

print(f"Part 2 - Squared numbers: {squared_numbers}")