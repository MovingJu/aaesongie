#include <iostream>

int main(){

    // new와 delete는 **항상 한 쌍**으로 활용한다. (memory leak방지)

    int *p_num = nullptr;

    p_num = new int;

    *p_num = 123;

    std::cout << "Addr: " << p_num << '\n';
    
    if(p_num != nullptr){
        std::cout << "valu: " << *p_num << '\n';
    }
    
    delete p_num;

    return 0;
}