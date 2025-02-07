#include <iostream>

int main(){

    std::string name;

    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    // int len_name = name.length();

    // bool emp_name = name.empty();

    // std::cout << name << std::endl;
    // std::cout << len_name << ", " << emp_name <<  std::endl;

    // name.append("@gmail.com");
    // std::cout << name << std::endl;

    // name.clear();
    // std::cout << name << std::endl;


    std::cout << name.at(2) << std::endl;
    std::cout << name.insert(1, "@") << std::endl;
    std::cout << name.find("@") << std::endl;
    std::cout << name.erase(0, 2) << std::endl;
    

    return 0;
}