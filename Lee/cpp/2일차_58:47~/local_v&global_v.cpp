#include <iostream>

// Global Variable 은 되도록 피하기.

int num = 3;

void printer(){

    int num = 2;

    std::cout << num << std::endl;
}

int main(){

    int num = 1;

    printer();

    std::cout << num << std::endl;

    std::cout << ::num << std::endl;

    return 0;
}