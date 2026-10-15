def count_vowels(s):
    vowels = "aeiouAEIOU"
    if s == "":
        return 0
    
    if s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return 0 + count_vowels(s[1:])
    

phrase = input("Enter anything to count vowel letters:  ")
result = count_vowels(phrase)
print(result)