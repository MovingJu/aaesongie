#include <iostream>

int search(int li[], int size, int mynum){


    for(int i=0; i<size; i++){
        if(mynum==li[i]){

            return i;
        }
    }
    
    return -1;
}

int main(){

    int seq[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(seq)/sizeof(int);
    int index;
    int mynum;

    std::cout << "Enter (0-10) #: ";
    std::cin >> mynum;

    index = search(seq, size, mynum);

    std::cout << index << std::endl;

    return 0;
}