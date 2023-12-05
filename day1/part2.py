# def check_digit(w):
#     if "one".startswith(w):
#         if w == "one":
#             return "1"
#         else:
#             return True

#     elif "two".startswith(w):
#         if w == "two":
#             return "2"
#         else:
#             return True

#     elif "three".startswith(w):
#         if w == "three":
#             return "3"
#         else:
#             return True

#     elif "four".startswith(w):
#         if w == "four":
#             return "4"
#         else:
#             return True

#     elif "five".startswith(w):
#         if w == "five":
#             return "5"
#         else:
#             return True

#     elif "six".startswith(w):
#         if w == "six":
#             return "6"
#         else:
#             return True

#     elif "seven".startswith(w):
#         if w == "seven":
#             return "7"
#         else:
#             return True

#     elif "eight".startswith(w):
#         if w == "eight":
#             return "8"
#         else:
#             return True

#     elif "nine".startswith(w):
#         if w == "nine":
#             return "9"
#         else:
#             return True
#     else:
#         return False

# with open("test_line.txt") as file:
#     lines = file.readlines()
# index = 1
# sum = 0

# for line in lines:
#     start = 0
#     end = 0
#     i = 0

#     while (i < len(line)):
#         char = line[i]
#         if(char.isdigit()):
#             if start == 0:
#                 start = char
#                 end = char
#             else:
#                 end = char
#             i = i + 1

#         else:
#             start_index = i
#             end_index = i + 1
#             check_valid = True
#             while(check_valid):
#                 digit = check_digit(line[start_index:end_index])
#                 if(type(digit) == bool and digit == False):
#                     i += 1
#                     check_valid = False
#                 else:
#                     if type(digit) == str:
#                         if start == 0:
#                             start = digit
#                             end = start
#                         else:
#                             end = digit

#                         check_valid = False

#                     else:
#                         end_index += 1
#                         check_valid_digit = check_digit(line[start_index:end_index])
#                         if(type(check_valid_digit) == bool and check_valid_digit == False):
#                             check_valid = False

#                     i += 1

#     print(str(index) + " = ", start + end)
#     sum = sum + int(start + end)
#     index += 1

# print("Sum = ", sum)

def check_digit_start(w, start_from):
    if(start_from == "start"):
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
    else:
        if "one".endswith(w):
            if w == "one":
                return "1"
            else:
                return True

        elif "two".endswith(w):
            if w == "two":
                return "2"
            else:
                return True

        elif "three".endswith(w):
            if w == "three":
                return "3"
            else:
                return True

        elif "four".endswith(w):
            if w == "four":
                return "4"
            else:
                return True

        elif "five".endswith(w):
            if w == "five":
                return "5"
            else:
                return True

        elif "six".endswith(w):
            if w == "six":
                return "6"
            else:
                return True

        elif "seven".endswith(w):
            if w == "seven":
                return "7"
            else:
                return True

        elif "eight".endswith(w):
            if w == "eight":
                return "8"
            else:
                return True

        elif "nine".endswith(w):
            if w == "nine":
                return "9"
            else:
                return True
        else:
            return False


with open("test_input.txt") as file:
    lines = file.readlines()

sum = 0

for line in lines:
    start = 0
    end = 0
    i = 0
    while(i < len(line)):
        outer_break = False
        char = line[i]
        if(char.isdigit()):
            start = char
            end = char
            break
        else:
            start_index = i
            end_index = i + 1
            check_valid = True
            while(check_valid):
                digit = check_digit_start(line[start_index:end_index], "start")
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
                        i += 1
                        outer_break = True
                        break

                    else:
                        end_index += 1
                        check_valid_digit = check_digit_start(line[start_index:end_index], "start")
                        if(type(check_valid_digit) == bool and check_valid_digit == False):
                            check_valid = False

                        i += 1


        if outer_break == True:
            break

    i = len(line)
    while(i >= 0):
        outer_break = False
        char = line[i - 1]
        if(char.isdigit()):
            end = char
            break
        else:
            start_index = i - 1
            end_index = i
            check_valid = True

            while(check_valid):
                digit = check_digit_start(line[start_index:end_index], "end")
                if(type(digit) == bool and digit == False):
                    i -= 1
                    check_valid = False
                else:
                    if type(digit) == str:
                        end = digit
                        check_valid = False
                        i -= 1
                        outer_break = True
                        break

                    else:
                        start_index -= 1
                        check_valid_digit = check_digit_start(line[start_index:end_index], "end")
                        if(type(check_valid_digit) == bool and check_valid_digit == False):
                            check_valid = False
                            i -= 1

        if outer_break == True:
            break


    # print("Number = ", int(str(start) + str(end)))
    sum = sum + int(str(start) + str(end))

print("Sum = ", sum)