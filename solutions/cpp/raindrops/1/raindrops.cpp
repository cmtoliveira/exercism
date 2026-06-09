#include "raindrops.h"

namespace raindrops {

// TODO: add your solution here
std::string convert (int number) {
    bool divisible_by_3 = number%3 == 0;
    bool divisible_by_5 = number%5 == 0;
    bool divisible_by_7 = number%7 == 0;
    std::string sound = "";
    
    if (divisible_by_3) sound += "Pling";
    if (divisible_by_5) sound += "Plang";
    if (divisible_by_7) sound += "Plong";
    if (sound.empty()) { 
        return std::to_string(number);
    }
    return sound;
}
}  // namespace raindrops
