// Fighting so long with C++ compiler and getting anxious, stressed and
// depressed about everything, I didn't comment anything and just wanted
// everything to work...

#include <iostream>
#include <fstream>
#include <string>

bool isCharInArray(char target, const char* charArray, size_t arraySize) {
    for (size_t i = 0; i < arraySize; ++i) {
        if (charArray[i] == target) {
            return true;  // Character found in the array
        }
    }
    return false;  // Character not found in the array
}

int formIntFromString(std::string textline) {
    char numbers[10] = {'0','1','2','3','4','5','6','7','8','9'};
    int i;
    bool is_number_found = false;
    char first_num = 'N';
    char last_num = 'N';
    int intline;

    for (i = 0; i < textline.length(); i++) {
        is_number_found = isCharInArray(textline[i], numbers, 10);
        if (is_number_found && first_num == 'N') {
            first_num = textline[i];
        } else if (is_number_found && first_num != 'N') {
            last_num = textline[i];
        }
    }

    if (last_num == 'N') {
        last_num = first_num;
    }
    intline = (first_num - '0')*10 + (last_num - '0');

    return intline;
}

int main() {

    std::ifstream inputFile("input.txt");

        // Check if the file is open
        if (!inputFile.is_open()) {
            std::cerr << "Error opening file." << std::endl;
            return 1; // Return an error code
        }

        // Read the file content line by line
        std::string line;
        int lineint;
        int sum = 0;

        while (std::getline(inputFile, line)) {
            lineint = formIntFromString(line);
            sum += lineint;
        }
        // Close the file when done
        inputFile.close();

        std::cout << sum << std::endl;
}