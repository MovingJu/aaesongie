#include <iostream>

class Stove{
    
    private:
        int temp = 0;


    public:

        Stove(int temp){
            set_temp(temp);
        }

        void get_temp(){
            std::cout << temp << '\n';
        }
        void set_temp(int temp);
};

void Stove::set_temp(int temp){
    this->temp = temp;
    }
    
int main(){

    Stove stove1(100);
    stove1.get_temp();

    return 0;
}