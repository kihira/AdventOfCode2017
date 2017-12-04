#include <iostream>
#include <vector>

int loop(int value, int max) {
    while (value >= max) value -= max;
    return value;
}

int main() {
    std::string in;
    std::cin >> in;

    std::vector<int> numbers;

    for (char i : in) {
        numbers.push_back(i - '0');
    }

    int sum = 0;
    int step = numbers.size() / 2;
    for (int i = 0; i < numbers.size(); i++) {
        int nextNum = numbers[loop(i + step, numbers.size())];
        if (numbers[i] == nextNum) {
            sum += numbers[i];
        }
    }

    std::cout << sum << std::endl;

    return 0;
}