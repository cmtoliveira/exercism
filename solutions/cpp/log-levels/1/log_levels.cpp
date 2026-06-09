#include <string>

namespace log_line {
std::string message(std::string line) {
    // return the message
    std::string lineMessage = line.substr(line.find(" ") + 1);
    return lineMessage;
    }

std::string log_level(std::string line) {
    // return the log level
    std::string lineLevel = line.substr(1,line.find("]") - 1);
    return lineLevel;
    }

std::string reformat(std::string line) {
    // return the reformatted message
    return message(line) + " (" + log_level(line) + ")";
    }
}  // namespace log_line
