#include "leap.h"

namespace leap {
    bool is_leap_year (int year) {
        bool divisible_by_4 = year%4 == 0;
        bool divisible_by_100 = year%100 == 0;
        bool divisible_by_400 = year%400 == 0;
        bool leap = ((divisible_by_4 and not divisible_by_100) == true) or ((divisible_by_100 and divisible_by_400) == true);
        return leap;
    }
} // namespace leap