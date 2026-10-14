#Task one 
def claclaut_vowels(text):
    
    if text=="":
        return 0
    
    if text[0].lower() in "a,e,i,o,u":
        return 1+claclaut_vowels(text[1:])
      
    return claclaut_vowels(text[1:])

print(claclaut_vowels("i love python"))



print("-"*50)


#Task 2 
numbers=[40,35,10,15,20]

mutliplied_numbers=list(map (lambda num:num*num, numbers))
print(mutliplied_numbers)