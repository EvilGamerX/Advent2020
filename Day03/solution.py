with open('./Day03/input.txt') as f:
        content = [i.strip() for i in f.readlines()]

trees = 0
rightPos = 0
loopMod = len(content[0])

for row in content:
    if row[rightPos] == '#':
        trees += 1
    rightPos = (rightPos + 3) % loopMod

print(f'The number of trees you hit are: {trees}')

