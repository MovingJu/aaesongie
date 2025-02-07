#include <iostream>

enum Months{
    jan,
    feb,
    mar,
    apr = 4,
    may,
    jun,
    jul,
    aug,
    sep,
    oct,
    nov,
    dec
};

int main(){
    Months today = jan;


    switch (today){
    case jan:
        std::cout << "Correct" << '\n';
        break;

    case 4:
        std::cout << "Close" << '\n';
        break;

    default:
        std::cout << "Nope" << '\n';
        break;
    }


    return 0;
}