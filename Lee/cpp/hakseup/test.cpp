#include <iostream>

int main(){

    // int arr[] = {10, 20, 30, 40}; 
    std::string arr[] = {"1", "2", "3", "4", "5"};

    std::string* p = arr;
    std::cout << *(p + 2) << std::endl;


    return 0;
}