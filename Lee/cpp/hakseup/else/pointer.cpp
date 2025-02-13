#include <iostream>

void reverser(int input[], int &size){

    int* arr1 = new int[size];

    for(int i=0; i<size; i++){
        arr1[i] = input[i];
    }

    for(int i=0; i<size; i++){
        input[i] = arr1[size - 1 - i];
    }

    delete[] arr1;
}

int main(){

    int size;

    std::cout << "Size of integer array?: ";
    std::cin >> size;

    int* arr = new int[size];

    for(int i=0; i<size; i++){
        std::cout << "Enter #" << i + 1 << ": ";
        std::cin >> arr[i];
    }

    reverser(arr, size);

    for(int i=0; i<size; i++){
        std::cout << arr[i] << " ";
    }

    delete[] arr;


    return 0;
}