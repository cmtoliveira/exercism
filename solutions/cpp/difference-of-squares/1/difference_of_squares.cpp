#include "difference_of_squares.h"
#include <cmath>

namespace difference_of_squares {
    int square_of_sum (int numbers) {
        int total = 0;
        for (int i = 1; i <= numbers; i++) {
            total += i;
        }
        return int(pow(total,2));
    }
    int sum_of_squares (int numbers) {
        int total = 0;
        for (int i = 1; i <= numbers; i++) {
            total += pow(i,2);
        }
        return total;
    }
    int difference (int numbers) {
        return square_of_sum(numbers) - sum_of_squares(numbers);
    }
}  // namespace difference_of_squares    
