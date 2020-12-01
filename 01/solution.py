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