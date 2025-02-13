#include <iostream>

void twotimer(int* a){
    *a *= 2;
}

void list_applyer(int* a, int size, void (*func)(int*)){

    for(int i=0; i < size; i++){
        func(a + i);
    }
}

int main(){


    int *p_names = nullptr;
    int size;

    std::cout << "How many inputs?: ";
    std::cin >> size;

    p_names = new int[size];

    for(int i=0; i<size; i++){
        std::cout << "Enter #: ";
        std::cin >> p_names[i];
    }
    
    for(int i=0; i<size; i++){
        std::cout << p_names[i] << ", ";
    }
    std::cout << '\n';

    list_applyer(p_names, size, twotimer);

    for(int i=0; i<size; i++){
        std::cout << p_names[i] << ", ";
    }
    std::cout << '\n';

    delete[] p_names;
    

    return 0;
}