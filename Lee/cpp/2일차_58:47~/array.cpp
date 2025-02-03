#include <iostream>

int main(){

    std::string stu[] = {"Lee", "Hwang", "Yun"};

    stu[2] = "Kim";
    std::cout << stu[0] << '\n';
    std::cout << stu[1] << '\n';
    std::cout << stu[2] << '\n';

    int num[3];

    num[0] = 1;
    num[1] = 2;
    num[2] = 3;

    std::cout << num[0] << '\n';
    std::cout << num[1] << '\n';
    std::cout << num[2] << '\n';


    return 0;
}