#include <iostream>

int main(){
    // new와 delete는 **항상 한 쌍**으로 활용한다. (memory leak방지)

    using str = std::string;

    str *p_names = nullptr;
    int size;

    std::cout << "How many inputs?: " << '\n';
    std::cin >> size;

    p_names = new str[size];

    for(int i=0; i<size; i++){
        std::cout << "Enter names: " << '\n';
        std::getline(std::cin >> std::ws, p_names[i]);
    }
    
    for(int i=0; i<size; i++){
        std::cout << p_names[i] << '\n';
    }

    delete[] p_names;
    

    return 0;
}