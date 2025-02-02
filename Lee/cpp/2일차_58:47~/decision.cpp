#include <iostream>

int main(){

    // int age;

    // std::cout << "Your age?: ";
    // std::cin >> age;

    // if (age >= 19){
    //     std::cout << "You're an adult." << std::endl;
    // }
    // else if (age < 0){
    //     std::cout << "You haven't been born yet!" << std::endl;
    // }
    // else {
    //     std::cout << "Get out." << std::endl;
    // }



    // int month;

    // std::cout << "Input month: ";
    // std::cin >> month;

    // switch (month) {
    //     case 1:
    //         std::cout << "It's Jan." << std::endl;
    //         break;
    //     case 2:
    //         std::cout << "It's Feb." << std::endl;
    //         break;
    //     case 3:
    //         std::cout << "It's Mar." << std::endl;
    //         break;
    //     case 4:
    //         std::cout << "It's Apr." << std::endl;
    //         break;
    //     case 5:
    //         std::cout << "It's May." << std::endl;
    //         break;
    //     case 6:
    //         std::cout << "It's Jun." << std::endl;
    //         break;
    //     case 7:
    //         std::cout << "It's Jul." << std::endl;
    //         break;
    //     case 8:
    //         std::cout << "It's Aug." << std::endl;
    //         break;
    //     case 9:
    //         std::cout << "It's Sep." << std::endl;
    //         break;
    //     case 10:
    //         std::cout << "It's Oct." << std::endl;
    //         break;
    //     case 11:
    //         std::cout << "It's Nov." << std::endl;
    //         break;
    //     case 12:
    //         std::cout << "It's Dec." << std::endl;
    //         break;
    //     default:
    //         std::cout << "Invalid month." << std::endl;
    //         break;
    // }


    // char grade;

    // std::cout << "Input grade: ";
    // std::cin >> grade;

    // switch (grade){
    //     case 'A':
    //         std::cout << "Normal" << std::endl;
    //         break;
        
    //     default:
    //         std::cout << "Failure." << std::endl;
    //         break;
    // }


    int num = 11;

    num % 2 == 0 ? std::cout << "Even" : std::cout << "Odd" << std::endl;

    std::cout << (num % 2 == 0 ? "Even" : "Odd") << std::endl;

    return 0;
}