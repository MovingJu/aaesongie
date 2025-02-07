#include <iostream>

int main(){

    int arr[100];

    std::fill(arr, arr + 100, 0);

    int i = 0;

    for(int val : arr){
        std::cout << val << ", " << i << '\n';
        i += 1;
    }


    return 0;
}