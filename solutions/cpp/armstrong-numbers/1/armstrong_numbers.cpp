#include "armstrong_numbers.h"
#include <string>
#include <cmath>

namespace armstrong_numbers {
    bool is_armstrong_number (int number) {
        std::string str_number = std::to_string(number);
        int total = 0;
        for (char num : str_number) {
            int char_to_int = num - '0';
            total += pow(char_to_int, str_number.size());
        }
        return total == number;
    }
}  // namespace armstrong_numbers