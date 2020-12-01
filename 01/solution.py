with open('./01/input.txt') as f:
    content = [i.strip() for i in f.readlines()]

doubled = []

for i, x in enumerate(content):
    i+=1
    for y in content[i:]:
        doubled.append((int(x), int(y)))

for pair in doubled:
    if(pair[0] + pair[1] == 2020):
        doubleAnswer = pair[0] * pair[1]
        break

print(f'The answer for the double is: {doubleAnswer}')

triple = []

for i, x in enumerate(content):
    i+=1
    for j, y in enumerate(content[i:]):
        j+=1
        for z in content[j:]:
            triple.append((int(x), int(y), int(z)))

for pair in triple:
    if(pair[0] + pair[1] + pair[2] == 2020):
        tripleAnswer = pair[0] * pair[1] * pair[2]
        break


print(f'The answer for the triple is: {tripleAnswer}')