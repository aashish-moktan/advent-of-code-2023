import re

with open("input.txt") as file:
    lines = file.readlines()

# Part 1
# sum = 0
# for line in lines:
#     start = 0
#     end = 0
#     for i in range(len(line)):
#         char = line[i]
#         if(char.isdigit()):
#             if(start == 0):
#                 start = char
#                 end = start
#             else:
#                 end = char

#     sum = sum + int(start + end)

# Part 2
def check_digit(word):
    if word in "one":
        return 1
    elif word in "two":
        return 2
    elif word in "three":
        return 3
    elif word in "four":
        return 4
    elif word in "five":
        return 5
    elif word in "six":
        return 6
    elif word in "seven":
        return 7
    elif word in "eight":
        return 8
    elif word in "nine":
        return 9


sum = 0
for line in lines:
    start = 0
    end = 0
    for i in range(len(line)):
        char = line[i]
        if(char.isdigit()):
            if(start == 0):
                start = check_digit(char)
                end = start
            else:
                end = check_digit(char)

    sum = sum + int(start + end)
