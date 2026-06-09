#include <string>

namespace log_line {
std::string message(std::string line) {
    // return the message
    int startIndex = line.find(" ") + 1;
    return line.substr(startIndex);
    }

std::string log_level(std::string line) {
    // return the log level
    int endIndex = line.find("]") - 1;
    return line.substr(1,endIndex);
    }

std::string reformat(std::string line) {
    // return the reformatted message
    return message(line) + " (" + log_level(line) + ")";
    }
}  // namespace log_line
