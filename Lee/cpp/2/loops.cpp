#include <iostream>

int main(){

    // std::string name;

    // while(name.empty()){
    //     std::cout << "Enter your name: ";
    //     std::getline(std::cin, name);
    // }

    // std::cout << "hellow, " << name << std::endl;



    // int num;

    // do {
    //     std::cout << "Enter positive #: ";
    //     std::cin >> num;
    // } while(num < 0);



    // for(int i = 0; i <= 10; i++){
    //     std::cout << i << '\n';
    //     continue;
    //     break;
    // }

    // std::cout << "Hellow world!" << std::endl;


    for(int i=0; i<=5; i++){
        for(int j=0; j<=i; j++){
            std::cout << "*";
        }
        std::cout << "\n";
    }

    

    return 0;
}