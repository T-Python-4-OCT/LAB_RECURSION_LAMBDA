# RECURSION
def vowels(phrase):
    if phrase == "":
        return 0
    if phrase[0].lower() in "aeiou":
        return 1 + vowels(phrase[1:])
    else:
        return vowels(phrase[1:])


print(vowels("I love python"))
    
# LAMBDA

numbers = [40, 35, 10, 15, 20]

new_list = list(map(lambda x: x * x, numbers))
print(new_list)