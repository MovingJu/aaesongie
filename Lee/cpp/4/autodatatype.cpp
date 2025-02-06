#include <iostream>

template <typename ty, typename pe>

auto max(ty x, pe y){
    return (x>y) ? x : y;
}

int main(){

    std::cout << max(1, '2') << std::endl;

    return 0;
}