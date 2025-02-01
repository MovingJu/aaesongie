#include <iostream>
#include <cmath>

int main(){

    double x, y, z;

    std::cout << "Enter side a: ";
    std::cin >> x;

    std::cout << "Enter side b: ";
    std::cin >> y;

    z = sqrt(pow(x, 2) + pow(y, 2));

    std::cout << z << std::endl;


    return 0;
}