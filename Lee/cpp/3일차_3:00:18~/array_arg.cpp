#include <iostream>

double getsum(double price[], int size){

    double sum;
    
    for(int i=0; i<size; i++){
        sum += price[i];
    }

    return sum;
}


int main(){

    double price[] = {4.99, 100, 1.13, 4.98, 100};

    int size = sizeof(price)/sizeof(double);

    double sum = getsum(price, size);

    std::cout << sum << std::endl;

    return 0;
}