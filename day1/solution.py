import re

numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

def get_pos(line):
    nums = []
    for i in range(len(numbers)):
        pos = line.find(numbers[i])
        indices = [match.start() for match in re.finditer(numbers[i], line)]
        for z in indices:
            if (z >= 0):
                nums.append((z, i + 1))

    for i in range(len(digits)):
        pos = line.find(digits[i])
        indices = [match.start() for match in re.finditer(digits[i], line)]
        for z in indices:
            if (z >= 0):
                nums.append((z, i + 1))

    return ((min(nums, key=lambda x: x[0]), max(nums, key=lambda x: x[0])))

def get_num(line):
    pos = get_pos(line)
    print("Position = ", pos)
    return (str(pos[0][1])+str(pos[1][1]))

sum = 0
with open("example_input.txt") as f:
    for line in f:
        sum += int(get_num(line))

print(sum)