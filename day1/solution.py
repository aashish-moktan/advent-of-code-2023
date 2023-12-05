import re
def puzzle_two():
    regex = r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|[0-9]))"
    number_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    result_sum = 0
    with open("input.txt", "r", encoding="utf_8") as input_file:
        for line in input_file:
            number_list = [
                number_dict[num] if num in number_dict else num
                for num in re.findall(regex, line)
            ]
            number = int(number_list[0] + number_list[-1])
            result_sum += number
    return result_sum

print(puzzle_two())