def count_vowels(phrase):
    if not phrase:
        return 0
    
    vowels = "aeiouAEIOU"
    
    current = 1 if phrase[0] in vowels else 0
    
    return current + count_vowels(phrase[1:])

print(count_vowels("I love python"))  
print("_"*20)

numbers = [40, 35, 10, 15, 20]

squared_numbers = list(map(lambda x: x * x, numbers))


print(squared_numbers)