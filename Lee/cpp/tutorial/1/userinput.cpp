#include <iostream>

int main(){

    std::string name;
    int age;

    std::cout << "Your name?: ";
    // std::cin >> name; 띄어쓰기를 받아들일 수 없음.
    std::getline(std::cin >> std::ws, name); 
    // getline위에 cin이 있을 경우 버퍼에 \n이 들어와 버리므로, 이를 제거하기 위한
    // >> std::ws 임.

    std::cout << "Your age?: ";
    std::cin >> age;

    std::cout << "hellow! " << name << age <<std::endl;    

    return 0;
}