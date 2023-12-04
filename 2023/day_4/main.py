import re
file = open('input.txt', 'r')
answer = 0
cardCount = 0
copies = {

}
for line in file:
    curr = line.split(":")
    print("Current card is ", curr[0])
    numbers = curr[1].split("|")
    cardId = re.findall(r'\d+', curr[0])[0]
    winners = re.findall(r'\d+', numbers[0])
    guesses = re.findall(r'\d+', numbers[1])
    points = 0
    matches = 0
    for guess in guesses:
        if guess in winners:
            matches += 1
            if points != 0:
                points *= 2
            else:
                points = 1
    currCopies = copies.get(cardId, 0) + 1
    print("Current copies of the card are ", currCopies)
    print("Current mathces on the card are ", currCopies)
    if matches != 0:
        print([x for x in range(1,matches + 1)])
        for num in range(1, matches + 1):
            print(num)
            copyId = int(cardId) + num
            print("Adding copies to card id ", copyId)
            if str(copyId) not in copies:
                copies[str(copyId)] = 1 * currCopies
            else:
                copies[str(copyId)] += 1 * currCopies
    cardCount += currCopies
    answer += points
print(copies)
print(cardCount)