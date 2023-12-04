import re
f = open('input.txt', 'r')
conversion = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}
def convert(elem):
    return conversion.get(elem, elem)


answer = 0
for line in f:
    print("Current line is: " + line)
    curr2 = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    print("All found are ", curr2)
    print("Lowest digit is: " + curr2[0])
    print("Highest digit is: " + curr2[-1])
    answer += int(convert(curr2[0]) + convert(curr2[-1]))
    print("Answer at the moment: " + str(answer))
print("The final answer is: " + str(answer))


