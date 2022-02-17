import json
with open("./record.json") as file:
    text = file.read()
    scoreorder = json.loads(text)['list']

with open('./wordlist.json') as file:
    answer = json.loads(file.read())['ans']

allchar = 'q w e r t y u i o p l k j h g f d s a z x c v b n m'.split()
print(len(allchar))
delete = []
for word in scoreorder:
    for char in allchar:
        if word[1].count(char) > 1 and word not in delete:
            delete.append(word)
    if word[1] not in answer and word not in delete:
        delete.append(word)
for d in delete:
    scoreorder.remove(d)
print(scoreorder[0])
for i in range(10):
    print(scoreorder[i][1], scoreorder[i][0])
