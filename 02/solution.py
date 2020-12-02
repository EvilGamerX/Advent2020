with open('./02/input.txt') as f:
    content = [i.strip() for i in f.readlines()]

validCount = 0

for line in content:
    spaceSplit = line.split(' ')
    occurences = [int(x) for x in spaceSplit[0].split('-')]
    letterCount = spaceSplit[2].count(spaceSplit[1][0])
    if occurences[0] <= letterCount and letterCount <= occurences[1]:
        validCount += 1

print(f'The number of valid passwords are: {validCount}')