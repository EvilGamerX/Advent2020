import math

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

rightJumps = [1, 3, 5, 7, 1]
downMods = [1, 1, 1, 1, 2]
trees = [0, 0, 0, 0, 0]
rightPositions = [0, 0, 0, 0, 0]


for i, row in enumerate(content):
    if row[rightPositions[0]] == '#':
        trees[0] += 1
    if row[rightPositions[1]] == '#':
        trees[1] += 1
    if row[rightPositions[2]] == '#':
        trees[2] += 1
    if row[rightPositions[3]] == '#':
        trees[3] += 1
    if not bool(i % downMods[4]):
        if row[rightPositions[4]] == '#':
            trees[4] += 1
        rightPositions[4] = (rightPositions[4] + rightJumps[4]) % loopMod
        
    for x in range(0, 4):
        rightPositions[x] = (rightPositions[x] + rightJumps[x]) % loopMod
        
print(f'The product of trees you hit are: {math.prod(trees)}')