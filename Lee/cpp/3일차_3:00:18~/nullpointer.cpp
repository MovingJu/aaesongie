#include <iostream>

int main(){

    // pointer를 사용할땐 항상 nullptr인지 아닌지 확인하는 조건문을 다는 것이 좋다.
    // nullptr을 dereference하면 큰 문제가 발생할수도?

    int *pointer = nullptr;
    
    int x = 123;
    pointer = &x;

    if(pointer != nullptr){
        std::cout << *pointer << std::endl;
    }

    return 0;
}