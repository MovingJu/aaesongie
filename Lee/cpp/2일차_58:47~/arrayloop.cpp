#include <iostream>

int main() {

    int num[] = {11, 12, 13, 14, 15, 16, 17};

    for(int numbers : num){
        std::cout << numbers << '\n';
    }

    return 0;
}