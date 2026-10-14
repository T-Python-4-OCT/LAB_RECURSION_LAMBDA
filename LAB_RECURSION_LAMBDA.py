def count_vowels(text):
    vowels = "aeiouAEIOU"
    if not text:
        return 0
    
    count = 1 if text[0] in vowels else 0
    return count + count_vowels(text[1:])

phrase = "I love python"
print(count_vowels(phrase))
##-----------------------------------------------------##
numbers = [40, 35, 10, 15, 20]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)