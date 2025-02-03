#include <iostream>

// int main(){

//     srand(time(NULL));

//     int num = rand() % 6;

//     std::cout << num << std::endl;

//     return 0;
// }

#include <ctime>

int main(){

    srand(time(0));

    int num = rand() % 6;

    std::cout << num << '\n';


    return 0;
}