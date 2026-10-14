''' Recursion: Count vowels '''

def vowels_count(word):
    if not word:
        return 0

    count = int(word[0].lower() in "aeiou")
    return count + vowels_count(word[1:])

print("Vowels count🔤:", vowels_count ("I love python"))
                                

'''Lambda + map: Square numbers '''

numbers = [40, 35, 10, 15, 20]

squares = list(map(lambda x: x ** 2, numbers))

print("Squared numbers: ",squares)