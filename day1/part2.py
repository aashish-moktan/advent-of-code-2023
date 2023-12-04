def check_digit(w):
    if "one".startswith(w):
        if w == "one":
            return "1"
        else:
            return True

    elif "two".startswith(w):
        if w == "two":
            return "2"
        else:
            return True

    elif "three".startswith(w):
        if w == "three":
            return "3"
        else:
            return True

    elif "four".startswith(w):
        if w == "four":
            return "4"
        else:
            return True

    elif "five".startswith(w):
        if w == "five":
            return "5"
        else:
            return True

    elif "six".startswith(w):
        if w == "six":
            return "6"
        else:
            return True

    elif "seven".startswith(w):
        if w == "seven":
            return "7"
        else:
            return True

    elif "eight".startswith(w):
        if w == "eight":
            return "8"
        else:
            return True

    elif "nine".startswith(w):
        if w == "nine":
            return "9"
        else:
            return True
    else:
        return False

with open("test_input.txt") as file:
    lines = file.readlines()
index = 1
sum = 0

for line in lines:
    start = 0
    end = 0
    i = 0

    while (i < len(line)):
        char = line[i]
        if(char.isdigit()):
            if start == 0:
                start = char
                end = char
            else:
                end = char
            i = i + 1

        else:
            start_index = i
            end_index = i + 1
            check_valid = True
            while(check_valid):
                digit = check_digit(line[start_index:end_index])
                if(type(digit) == bool and digit == False):
                    i += 1
                    check_valid = False
                else:
                    if type(digit) == str:
                        if start == 0:
                            start = digit
                            end = start
                        else:
                            end = digit

                        check_valid = False

                    else:
                        # if(len(line[start_index:end_index]) == 1):
                        #     end_index += 1
                        #     check_valid_digit = check_digit(line[start_index:end_index])
                        #     if(type(check_valid_digit) == bool and check_valid_digit == False):
                        #         check_valid = False

                        # else:
                        end_index += 1
                        check_valid_digit = check_digit(line[start_index:end_index])
                        if(type(check_valid_digit) == bool and check_valid_digit == False):
                            check_valid = False

                    i += 1

    print(str(index) + " = ", start + end)
    sum = sum + int(start + end)
    index += 1

print("Sum = ", sum)