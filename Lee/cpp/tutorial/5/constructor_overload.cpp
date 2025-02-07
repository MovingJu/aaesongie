#include <iostream>

class Pizza{
    public:
        std::string topping1 = "cheese";
        std::string topping2;
        std::string topping3;

    Pizza(){}
    Pizza(std::string topping1){
        this->topping1 = topping1;
    }
    Pizza(std::string topping1, std::string topping2){
        this->topping1 = topping1;
        this->topping2 = topping2;
    }

};

int main(){

    Pizza p1;
    Pizza p2("pepperoni");
    Pizza p3("pepperoni", "olive");

    std::cout << p1.topping1 << std::endl;
    std::cout << p2.topping1 << std::endl;
    std::cout << p3.topping2 << std::endl;

    return 0;
}