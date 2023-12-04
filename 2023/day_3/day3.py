import math
import re
file = open('input.txt', 'r')
data = file.read().splitlines()

def findPartNumSum(data):
    answer = 0
    for idx, line in enumerate(data):
        print("Starting next line...")
        prevLine = None
        nextLine = None
        if idx != 0:
            prevLine = data[idx - 1]
        if idx != len(data)-1:
            nextLine = data[idx + 1]
        nums = re.findall(r'\d+', line)
        if len(nums) == 0:
            continue
        print(prevLine)
        print(line)
        print(nextLine)
        for match in re.finditer(r'\d+', line):
            print("Searching number: ", match.group())
            start = match.start()
            end = match.end()
            if start != 0:
                start -= 1
            if end == len(line):
                end -= 1
            prevChar = line[start]
            print(end, len(line))
            nextChar = line[end]
            
            add = bool(re.search(r'[^a-zA-Z0-9.\s]', prevChar+nextChar))
            print(prevChar+nextChar, add)
            if (not add):
                if end < len(line)-1:
                    end += 1
                if prevLine:
                    subString = prevLine[start:end]
                    print(subString)
                    add = bool(re.search(r'[^a-zA-Z0-9.\s]', subString))
                if nextLine and not add:
                    subString2 = nextLine[start:end]
                    print(subString2)
                    add = bool(re.search(r'[^a-zA-Z0-9.\s]', subString2))

            if add:
                print("Adding number: ", match.group())
                answer += int(match.group())
    print("Ending current line...")
    
def findGearRatios(data):
    answer = 0
    for idx, line in enumerate(data):
        print("Starting next line...")
        prevLine = None
        nextLine = None
        if idx != 0:
            prevLine = data[idx - 1]
        if idx != len(data)-1:
            nextLine = data[idx + 1]
        if "*" not in line:
            continue
        print(prevLine)
        print(line)
        print(nextLine)
        for match in re.finditer(r'\*', line):
            start = match.start()
            end = match.end()
            row = 1
            nums = 0
            if end != len(line):
                for num in re.finditer(r'\d+', line):
                    if num.end() == start or num.start() == end:
                        row *= int(num.group())
                        nums += 1
                print(row)
            if start != 0:
                start -= 1
            if nums != 2:
                print('Checking other lines...')
                print(start, end)
                if prevLine:
                    print("Checking previous line...")
                    for num in re.finditer(r'\d+', prevLine):
                        numEnd = num.end() - 1
                        print("Checkng num: ", num.group())
                        print("The start is at ", num.start())
                        print("The end is at ", end)
                        if (numEnd >= start and numEnd <= end ) or (num.start() >= start and num.start() <= end ):
                            row *= int(num.group())
                            nums += 1
                    print(row)
                if nextLine and nums != 2:
                    print("Checking next line...")
                    for num in re.finditer(r'\d+', nextLine):
                        numEnd = num.end() - 1
                        print("Checkng num: ", num.group())
                        print("The start is at ", num.start())
                        print("The end is at ", numEnd)  
                        if (numEnd >= start and numEnd <= end ) or (num.start() >= start and num.start() <= end ) :
                            row *= int(num.group())
                            nums += 1
                    print(row)

            if nums == 2:
                answer += row
                print("At the moment the answer is ", answer)
        print("Ending current line...")
    print("The asnwer is ", answer)

findGearRatios(data)