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

    Coffee(std::string bean, bool is_cold, std::string x){
        this->bean = bean;
        this->is_cold = is_cold;
        cup = x;
    }
};

int main(){

    Coffee espresso("ethiopian", false, "Paper");
    Coffee americano("american", true, "Glass");

    std::cout << americano.bean << '\n';
    std::cout << espresso.bean << '\n';

    espresso.made(espresso.cup);

    // espresso.drip();
    // espresso.made(espresso.cup);

    return 0;
}