#include <iostream>

int main(){

    int students = 20;

    students = students + 1;
    students += 1;
    students++;

    students/=3;

    std::cout << students << std::endl;

    int remainder = students % 2;

    std::cout << remainder << std::endl;



    return 0;
}