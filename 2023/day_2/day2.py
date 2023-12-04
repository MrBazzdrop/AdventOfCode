import re
f = open('input.txt', 'r')
def findLeastPossible(file):
    answer = 0
    ids = 0
    bag = {
            "green": 13,
            "blue": 14,
            "red": 12
        }
    for line in file:
        minimums = {
            
        }
        print("Current game is " + line)
        curr = line.split(":")
        cubes = re.findall(r'(\d{1,2}\sred|\d{1,2}\sgreen|\d{1,2}\sblue)', curr[1])
        addGame = True
        for cube in cubes:
            amounts = cube.split(' ')
            if amounts[1] not in minimums:
                minimums[amounts[1]] = int(amounts[0])
            elif minimums[amounts[1]] < int(amounts[0]):
                minimums[amounts[1]] = int(amounts[0])
            if int(amounts[0]) > bag.get(amounts[1]):
                addGame = False
        power = 1
        for minimum in minimums.values():
            power *= minimum
        print("Current game power is " + str(power))
        answer += power
        if addGame:
            id = curr[0].split(" ")[1]
            print("The added game ID is " + id)
            ids += int(id)
        print("Current answer is: " + str(answer))
        print("Current IDs answer is: " + str(ids))
    print("Final answer is " + str(answer))
    print("Final IDs answer is " + str(ids))
findLeastPossible(f)