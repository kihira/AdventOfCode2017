#include <iostream>
#include <vector>

int main() {
    std::string in;
    std::cin >> in;

    std::vector<int> numbers;

    for (char i : in) {
        numbers.push_back(i - '0');
    }

    int currDigit = numbers[0];
    int sum = 0;
    for (int i = 1; i < numbers.size(); ++i) {
        if (numbers[i] == currDigit) {
            sum += currDigit;
        }
        else currDigit = numbers[i];
    }
    if (currDigit == numbers[0]) sum += currDigit;

    std::cout << sum << std::endl;

    return 0;
}