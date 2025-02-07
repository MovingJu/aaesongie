#include <iostream>

void twotimer(int* a){
    *a *= 2;
}

void squarer(int* a){
    *a = *a * *a;
}

void cuber(int* a){
    *a = *a * *a * *a;
}

void list_applyer(int* a, int size, void (*func)(int*)){

    for(int i=0; i < size; i++){
        func(a + i);
    }

}

int main(){

    int num[5] = {1, 2, 3, 4, 5};
    int num_size = sizeof(num)/sizeof(num[0]);
    int* p_num = &num[0];

    for(int n : num){
        std::cout << n << ", ";
    }
    std::cout << "\n";

    list_applyer(p_num, num_size, squarer);

    for(int n : num){
        std::cout << n << ", ";
    }


    return 0;
}