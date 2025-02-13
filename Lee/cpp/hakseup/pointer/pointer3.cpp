#include <iostream>

void swapPointer(int** pp_n1, int** pp_n2){

    int* temp = *pp_n1;
    *pp_n1 = *pp_n2;
    *pp_n2 = temp;
}

int main(){

    int n1 = 1;
    int n2 = 2;
    int* p_n1 = &n1;
    int* p_n2 = &n2;
    int** pp_n1 = &p_n1;
    int** pp_n2 = &p_n2;

    swapPointer(pp_n1, pp_n2);

    std::cout << n1 << ", " << n2 << std::endl;

    return 0;
}