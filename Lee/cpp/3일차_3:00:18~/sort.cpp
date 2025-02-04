#include <iostream>

using str = std::string;

str sort(int arr[], int size){

    int imsi;
    str result;

    for(int i=0; i<size; i++){
        for(int j=0 + i; j<size; j++){
            if(arr[i] > arr[j]){
                imsi = arr[j];
                arr[j] = arr[i];
                arr[i] = imsi;
            }
        }
    }

    for(int i=0; i<size; i++){
        result += std::to_string(arr[i]) + ' ';
    }

    return result;
}

int main(){

    int arr[] = {5, 10, 9, 6, 3, 4, 8, 7, 1, 2};
    int size = sizeof(arr)/sizeof(int);
    str sorted;

    sorted = sort(arr, size);

    std::cout << sorted << std::endl;

    return 0;
}