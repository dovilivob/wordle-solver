import json
import random
import time
with open('wordlist.json') as file:
    text = file.read()
    wordlist = json.loads(text)['list']


def ran(list):
    return random.randint(0, len(list)-1)


alphascore = [
    {'q': 78, 'w': 411, 'e': 303, 'r': 628, 't': 815, 'y': 181, 'u': 189, 'i': 165, 'o': 262, 'p': 857, 'a': 736, 's': 1560, 'd': 681,
        'f': 595, 'g': 637, 'h': 488, 'j': 202, 'k': 375, 'l': 575, 'z': 105, 'x': 16, 'c': 920, 'v': 242, 'b': 908, 'n': 325, 'm': 693},
    {'q': 15, 'w': 163, 'e': 1626, 'r': 940, 't': 239, 'y': 267, 'u': 1185, 'i': 1380, 'o': 2093, 'p': 228, 'a': 2260, 's': 93, 'd': 84,
        'f': 24, 'g': 75, 'h': 544, 'j': 11, 'k': 95, 'l': 697, 'z': 29, 'x': 57, 'c': 176, 'v': 52, 'b': 81, 'n': 345, 'm': 188},
    {'q': 13, 'w': 271, 'e': 882, 'r': 1197, 't': 615, 'y': 213, 'u': 666, 'i': 1047, 'o': 989, 'p': 363, 'a': 1235, 's': 531, 'd': 390,
     'f': 178, 'g': 362, 'h': 120, 'j': 46, 'k': 268, 'l': 848, 'z': 142, 'x': 133, 'c': 392, 'v': 240, 'b': 334, 'n': 962, 'm': 510},
    {'q': 2, 'w': 128, 'e': 2323, 'r': 716, 't': 897, 'y': 108, 'u': 401, 'i': 880, 'o': 696, 'p': 418, 'a': 1073, 's': 515, 'd': 471,
        'f': 233, 'g': 422, 'h': 235, 'j': 29, 'k': 500, 'l': 771, 'z': 126, 'x': 12, 'c': 406, 'v': 155, 'b': 242, 'n': 786, 'm': 402},
    {'q': 4, 'w': 64, 'e': 1519, 'r': 673, 't': 726, 'y': 1297, 'u': 67, 'i': 280, 'o': 388, 'p': 147, 'a': 679, 's': 3950, 'd': 822,
        'f': 82, 'g': 143, 'h': 367, 'j': 3, 'k': 257, 'l': 475, 'z': 32, 'x': 70, 'c': 127, 'v': 4, 'b': 59, 'n': 530, 'm': 182}
]
alph = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'.split()
answer = wordlist[ran(wordlist)]
current = wordlist[ran(wordlist)]
# current = 'crane'
state = 1
print(answer)
print()


while current != answer:
    state += 1
    delete = []
    for index, char in enumerate(current):
        if char in answer:
            for word in wordlist:
                if char not in word:
                    delete.append(word)
            if answer[index] == char:
                for word in wordlist:
                    if word[index] != char:
                        delete.append(word)
            else:
                for word in wordlist:
                    if word[index] == char:
                        delete.append(word)
        else:
            for word in wordlist:
                if char in word:
                    delete.append(word)
    for de in delete:
        if de in wordlist:
            wordlist.remove(de)
    result = wordlist.copy()
    if state < 3:
        for word in wordlist:
            for ch in alph:
                if word.count(ch) > 1 and word in result:
                    result.remove(word)
    compare = []

    alphadict = [{}, {}, {}, {}, {}]
    if len(wordlist) > 30:
        for i in range(5):
            for ch in alph:
                alphadict[i][ch] = 0
        for word in wordlist:
            for i in range(5):
                alphadict[i][word[i]] += 1
    else:
        alphadict = alphascore

    for word in result:
        n = 0
        for index, char in enumerate(word):
            n += alphadict[index][char]
        compare.append([n, word])
    compare.sort(reverse=True)
    print(current, len(wordlist))
    current = compare[0][1]
    # time.sleep(1)

print(current, state, sep=': ')
