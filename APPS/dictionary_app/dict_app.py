import json
# from difflib import SequenceMatcher # SequenceMatcher(None, 'rainn','rain').ratio() = this will return a ratio regarding how simillar the words are
from difflib import get_close_matches # uses SequenceMatcher to return a list of the best 'good enough' matches




# load the data from data.json in a dictionary with json.load function
data = json.load(open('data.json'))

# function to return the explanation of the word from the dictionary
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        match_found = get_close_matches(word, data.keys(), cutoff=0.8)[0]
        # function get_close_matches() returns 1st element of the list which is closest match to 'word', in the dictionary keys list
        answer = input("Did you mean '%s' instead? Answer 'Y' if yes, or 'N' if no: " % match_found)
        answer = answer.upper()
        if answer == 'Y':
            return data[match_found]
        elif answer == 'N':
            return "The word '%s' doesn't exit in dictionary. Please double check it." % word
        else:
            return "I didn't understand your query."
    else:
        return "The word '%s' doesn't exits in dictionary. Please double check it." % word

question = input('Enter a word: ')
output = translate(question)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)
