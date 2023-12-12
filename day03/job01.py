# Do NOT use this as an example, except maybe as a bad one
# A lot of playing with indexes and forming lists

# Save the indexes that contain symbols and digits
def markSymbolsAndDigits(str_line):
    # A list of chars that are not defined as symbols in this job
    digits = ["0", "1", "2", "3", "4", "5", "6" ,"7", "8", "9"]
    symbol_indx = []
    digit_indx = []

    i = 0
    while i < len(str_line):
        char = str_line[i]
        # Don't mind the dots
        if char != ".":
            if char in digits:
                digit_indx.append(i)
            else:
                symbol_indx.append(i)
        i += 1

    return symbol_indx, digit_indx


# Check if a symbol is near the digit
# It's a mess, but it checks previous, current and next symbol for
# previous current and next lines
def isDigitNearSym(digit, prev_symbols, current_symbols, next_symbols):
    if digit in prev_symbols or digit+1 in prev_symbols or digit-1 in prev_symbols \
        or digit in current_symbols or digit+1 in current_symbols or digit-1 in current_symbols \
        or digit in next_symbols or digit+1 in next_symbols or digit-1 in next_symbols:
        return True
    else:
        return False


# We need to first get all the indexes for correct numbers
# Then formulate the whole numbers from the text with our indexes
# And finally calculate the sum
def calculateSumFromDigits(near_symbol_digits, all_digits, textline):
    for index in all_digits:
        if index not in near_symbol_digits:
            


if __name__ == "__main__":
    # There are 140 chars (+ "\n") in every single line and 140 lines
    # So it's a 140x140 grid
    with open("C:\\Users\\Miika\\Documents\\AOC23\\day03\\input.txt", "r") as file:
        all_lines = file.readlines()

        i = 0
        while i < len(all_lines):
            # We have to handle first and last line separately
            # Map the symbols on previous, current and next line
            if i == 0:
                next_line = all_lines[i+1].strip("\n")

                prev_symbols, prev_digits = [], []
                next_symbols, next_digits = markSymbolsAndDigits(next_line)
            elif i >= 139:
                prev_line = all_lines[i-1].strip("\n")

                prev_symbols, prev_digits = markSymbolsAndDigits(prev_line)
                next_symbols, next_digits = [], []
            else:
                next_line = all_lines[i+1].strip("\n")
                prev_line = all_lines[i-1].strip("\n")

                prev_symbols, prev_digits = markSymbolsAndDigits(prev_line)
                next_symbols, next_digits = markSymbolsAndDigits(next_line)

            current_line = all_lines[i].strip("\n")
            current_symbols, current_digits = markSymbolsAndDigits(current_line)

            correct_digits = []
            for digit_i in current_digits:
                # Check if digit is near a symbol
                if isDigitNearSym(digit_i, prev_symbols, current_symbols, next_symbols):
                    correct_digits.append(digit_i)



            # Debugging
            #"""
            print("curr num", current_digits)
            print("prev sym", prev_symbols)
            print("curr sym", current_symbols)
            print("next sym", next_symbols)
            print()
            #"""

            i += 1