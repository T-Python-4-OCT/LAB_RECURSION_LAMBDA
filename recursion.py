def count_vowels(text):
  vowels = "aeiouAEIOU"

  if len(text) == 0:
    return 0

  if text[0] in vowels:
    return 1 + count_vowels(text[1:])
  else:
    return 0 + count_vowels(text[1:])


phrase = "I love python"
print(count_vowels(phrase)) 