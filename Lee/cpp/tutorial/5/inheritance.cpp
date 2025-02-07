#include <iostream>

class Animal{
    protected:
        bool alive = true;
        int legs;
    
    public:
        void eat(){
            std::cout << "Animal is eating." << '\n';
        }
        bool get_alive(){
            return alive;
        }
        void set_alive(bool alive){
            this->alive = alive;
        }
};

class Dog : public Animal{
    protected:
        std::string sound = "MungMung";
        std::string fur_color;

    public:
        Dog(){
            legs = 4;
        }

        void make_sound(){
            std::cout << sound << std::endl;
        }

        std::string get_fur_color(){
            return fur_color;
        }

        void set_fur_color(std::string fur_color){
            this->fur_color = fur_color;
        }
};

class Maltiz : public Dog{
    public:
        Maltiz(){
            fur_color = "White";
        }
};

class Cat : public Animal{
    protected:
        std::string sound = "Myaong";
        std::string fur_color;

    public:
        Cat(){
            legs = 4;
        }

        void make_sound(){
            std::cout << sound << std::endl;
        }

        std::string get_fur_color(){
            return fur_color;
        }

        void set_fur_color(std::string fur_color){
            this->fur_color = fur_color;
        }
};

int main(){

    Maltiz dodo;
    dodo.make_sound();
    dodo.set_alive(true);

    return 0;
}