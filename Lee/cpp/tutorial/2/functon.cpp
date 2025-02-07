#include <iostream>

// void hbd(std::string name, int age);

void square();
double square(double len);

int main(){

    // std::string name = "MovingJu";

    // int age = 19;

    // hbd(name, age);

    int len = 2;

    square();
    len = square(len);

    std::cout << len << std::endl;

    return 0;
}
void square(){
    std::cout << "Calculate square value of something." << std::endl;
}
double square(double len){
    return len * len;
}


// void hbd(std::string name, int age){

    // std::cout << "hbd to " << name << "\n";
    // std::cout << "hbd to " << name << "\n";
    // std::cout << "hbd to " << name << "\n";
    // std::cout << "happy my " << age << "th birth day.\n";

// }