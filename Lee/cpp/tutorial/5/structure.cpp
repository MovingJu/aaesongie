#include <iostream>

struct Students{
    std::string name;
    double gpa;
    bool enrolled = true;
};

int main(){

    Students stu1;
    stu1.name = "lee";
    stu1.gpa = 4.5;

    Students stu2;
    stu2.name = "chul";
    stu2.gpa = 1.0;
    stu2.enrolled = false;

    std::cout << stu1.name << "\n";
    std::cout << stu1.gpa << "\n";
    std::cout << stu1.enrolled << "\n";

    std::cout << stu2.name << "\n";
    std::cout << stu2.gpa << "\n";
    std::cout << stu2.enrolled << "\n";

    return 0;
}