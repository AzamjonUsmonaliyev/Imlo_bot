from uzwords import words
from difflib import get_close_matches


def checkWords(word,words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words,5))
    available = False

    if word in matches:
        available = True
        matches = word
    elif 'h' in word:
        word = word.replace('h','x')
        matches.update(get_close_matches(word,words))
    elif 'x' in word:
        word = word.replace('x','h')
        matches.update(get_close_matches(word,words))

    return {'available':available,'matches':matches}

if __name__ == '__main__':
    print(checkWords('азот'))
    print(checkWords('агноия'))
    print(checkWords('хато'))
    print(checkWords('ҳато'))

# print(get_close_matches('ҳўшшаймоқ',words,n=5))
# print(get_close_matches('агноия',words))

