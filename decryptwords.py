from collections import Counter

def compareLetters(word1, word2):
    check = 0
    compare1 = list(word1)
    compare2 = list(word2)
    for letter1 in compare1:
        if letter1 not in compare2:
            check +=1
    for letter2 in compare2:
        if letter2 not in compare1:
            check +=1
    if check != 0:
        return True
    else:
        return False

lines1 = [line.strip('\n') for line in open('wordlist.txt')]
lines2 = list(filter(None, [line.strip() for line in open('words.txt')]))
answer = []

for line2 in lines2:
    for line1 in lines1:
        letters1 = list(line1)
        letters2 = list(line2)
        combine = Counter(letters1 + letters2)
        unique = [n for n in combine if combine[n]==1]
        if len(unique) == 0 and len(line1) == len(line2) and compareLetters(line1, line2) == False:
            answer.append(line1)

print(','.join(answer))
