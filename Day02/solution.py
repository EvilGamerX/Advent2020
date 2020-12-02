def day02():
    with open('./Day02/input.txt') as f:
        content = [i.strip() for i in f.readlines()]

    validCount = 0

    for line in content:
        spaceSplit = line.split(' ')
        occurences = [int(x) for x in spaceSplit[0].split('-')]
        letterCount = spaceSplit[2].count(spaceSplit[1][0])
        if occurences[0] <= letterCount and letterCount <= occurences[1]:
            validCount += 1

    print(f'The number of valid passwords are: {validCount}')

    # Part 2
    validCount = 0

    for line in content:
        spaceSplit = line.split(' ')
        locations = [int(x) for x in spaceSplit[0].split('-')]
        checkLetter = spaceSplit[1][0]
        if (spaceSplit[2][locations[0] - 1] == checkLetter) ^ (spaceSplit[2][locations[1] - 1] == checkLetter):
            validCount += 1


    print(f'The number of valid passwords are: {validCount}')
