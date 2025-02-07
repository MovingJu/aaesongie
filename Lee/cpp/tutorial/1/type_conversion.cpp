#include <iostream>

int main(){

    // double x = (int) 3.14;

    // std::cout << x << std::endl;

    // std::cout << (char) 100 << std::endl;

    int correct = 8;
    int questions = 10;

    double score = (double)correct/questions * 100;

    std::cout << score << std::endl;

    return 0;
}