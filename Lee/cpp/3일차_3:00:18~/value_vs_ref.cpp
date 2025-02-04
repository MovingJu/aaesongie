#include <iostream>

void swapper(int &x, int &y){

    int temp;

    temp = x;
    x = y;
    y = temp;

}

void value(int x, int y){

    std::cout << &x << ", " << &y << '\n';
}

void address(int &x, int &y){

    std::cout << &x << ", " << &y << '\n';
}

int main(){

    int x = 0;
    int y = 1;

    std::cout << x << ", " << y << '\n';

    swapper(x, y);

    std::cout << x << ", " << y << '\n';

    std::cout << "**********************" << '\n';

    std::cout << &x << ", " << &y << '\n';

    value(x, y);

    std::cout << &x << ", " << &y << '\n';

    address(x, y);

    return 0;
}

