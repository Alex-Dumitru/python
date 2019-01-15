'''
Pig latin is a game of alternations played on the English language game. To
create the pig latin form of a word the initial consonant sound is transposed
to the end of the word and an 'ay' is affixed.
Example: "banana" would yield "ananabay".
Make a program that converts a word or a sentence to Pig Latin.
For added difficulty, if users input only numbers, notify them of a translation
error.
'''
def pig_latin(word):
    for letter in word:
        range = 0
        print(letter)
        # if 1st letter is voel, return the word appended with 'ay'
        if letter.lower() in 'aeiou':
            return word + 'ay'
        # if letter is voel, but a number of consonants already were found, then break the for loop
        elif letter.lower() in 'aeiou' and range > 0:
            break
        # consonant is found so increment range
        else:
            range += 1
    print(range)
    text = word[range+1:] + word[:range] + 'ay'
    return text
# get input from user
user_text = input('Enter text to translate to Pig Latin: ')
list_of_words = user_text.split()
pig_latin_text = ''
for word in list_of_words:
    pig_latin_text = pig_latin_text + pig_latin(word) + ' '
print(pig_latin_text)
