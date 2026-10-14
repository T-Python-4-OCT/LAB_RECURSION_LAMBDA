# recursion
def count_vowels(text):
    if not text:
        return 0
    return (text[0].lower() in "aeiou") + count_vowels(text[1:])

print(count_vowels(input("Enter a word or phrase: ")))

# Lambda
num = [40,35, 10, 15, 20]
new_list = list(map(lambda x: x * x, num))
print(new_list)