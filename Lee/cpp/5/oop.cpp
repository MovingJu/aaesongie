#include <iostream>

class Coffee{
    public:
        std::string bean;
        bool is_cold = false;
        std::string cup;

        void drip(){
            std::cout << "Coffee is being made." << '\n';
        }
        void made(std::string &cup){
            std::cout << "Take your Coffee in ." << cup << " cup." << '\n';
        }
};

int main(){

    Coffee espresso;
    espresso.bean = "Korean";
    espresso.cup = "Glass";
    Coffee americano;
    americano.bean = "american";

    std::cout << americano.bean << '\n';
    std::cout << espresso.bean << '\n';

    // espresso.drip();
    // espresso.made(espresso.cup);

    return 0;
}