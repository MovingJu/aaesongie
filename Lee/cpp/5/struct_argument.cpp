#include <iostream>

struct Cars{
    std::string name;
    int year;
    std::string color;
};

void printer(Cars &car){

    std::cout << car.name << '\n';
    std::cout << car.year << '\n';
    std::cout << car.color << '\n';
    std::cout << &car << '\n';

}


int main(){

    Cars car1;
    car1.name = "Hyundai";
    car1.year = 2024;
    car1.color = "silver";


    Cars car2;
    car2.name = "Ferarri";
    car2.year = 2025;
    car2.color = "red";

    printer(car1);
    std::cout << &car1 << '\n';

    return 0;
}