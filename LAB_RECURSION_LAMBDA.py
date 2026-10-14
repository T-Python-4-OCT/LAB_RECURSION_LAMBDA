
def count_vowels(phrase):
    if not phrase:
        return 0
    
    vowels = "aeiou"
    is_vowel = 1 if phrase[0].lower() in vowels else 0
    
    return is_vowel + count_vowels(phrase[1:])

phrase_example = "I love python"
print(f"Phrase: '{phrase_example}'")
print(f"Vowels count: {count_vowels(phrase_example)}")


print("-" * 42)

numbers = [40, 35, 10, 15, 20]

squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Original list:", numbers)
print("Squared list:", squared_numbers)