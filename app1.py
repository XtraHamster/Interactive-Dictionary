import json
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        mistake = input(f'Did you mean {get_close_matches(w, data.keys())[0]} instead? (Type Y for yes / N for no): ')
        if mistake == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif mistake == 'N':
            return 'The word does not exist.'
        else:
            return 'We did not understand your entry'
    else:
        return 'The word does not exist.'

word = input('Enter word: ')

output = translate(word)

if type(output) == list:    
    for i in output:
        print(i)
else:
    print(output)