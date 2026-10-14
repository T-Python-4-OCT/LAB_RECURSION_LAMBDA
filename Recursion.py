def VowelsCounter(word) :
  if word == "" :
    return 0

  if word[0].lower() in "aeiou" :
    return VowelsCounter(word[1:]) + 1
  else :
    return VowelsCounter(word[1:])


print(VowelsCounter('iiiioooiiieee'))