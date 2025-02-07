#include <iostream>

void printinfo(const std::string &name, const int &age){
    std::cout << name << ", " << age << '\n';
}

int main(){

    std::string name = "MovingJu";
    int age = 19;

    printinfo(name, age);

    return 0;
}