
# Advent of Code 2023: Day 1, Job 2
# This time in Python because I suck at C++

# A way too long function to get our desired in value from a line of text
def fromStringToInt(lineoftext):
    # We need these lists to handle all the numbers
    # It's handy to have their indexes match: digits[0] = 0, digit_strings[0] = "0" etc
    digit_strings = ["NOT_IN_USE", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    number_strings = ["NOT_IN_USE", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer_list = []

    # Build a list full of 'X' to be replaced to we can fit found digits in order
    for char in lineoftext:
        answer_list.append("X")

    # First check for digits in the line
    for digit in digit_strings:
        try:
            index = lineoftext.find(digit)
            while index != -1:
                answer_list[index] = digit
                # To the next occurence
                index = lineoftext.find(digit, index + 1)
        except ValueError:
            pass
    # Then for number strings
    for number in number_strings:
        try:
            index = lineoftext.find(number)
            # Search for every occurence
            while index != -1:
                # We need to "transform" the written number into a digit and add it to the list
                num_index = number_strings.index(number)
                answer_list[index] = digit_strings[num_index]
                # Moving to next occurence
                index = lineoftext.find(number, index + 1)
        except ValueError:
            pass
        except TypeError:
            pass

    # Remove all 'X' from our list so we can easily find first and last digits
    answer_list = [item for item in answer_list if item != 'X']

    # Transform strings into ints
    i = 0
    while(i < len(answer_list)):
        answer_list[i] = int(answer_list[i])
        i += 1

    # Find and form first and last digits
    first_digit = answer_list[0]
    if len(answer_list) == 1:
        last_digit = first_digit
    else:
        last_digit = answer_list[ ( len(answer_list) - 1 ) ]

    # Finally, out answer
    correct_int = 10*first_digit + last_digit
    return correct_int


if __name__ == "__main__":
    # Open file to be used
    input_file = open("C:\\Users\\Miika\\Documents\\AOC23\\day01\\input.txt", "r")

    # Hande the file line by line
    sum = 0
    for line in input_file:
        linesum = fromStringToInt(line)
        sum += linesum
        # For debugging
        # print(f"linesum: {linesum}")
    print(sum)

    input_file.close()