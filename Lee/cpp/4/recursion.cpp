#include <iostream>

int fibonacci(int n){

    int result = 0;

    if(n == 1){
        return 1;
    }
    else if (n == 2){
        return 2;
    }
    else{
        return result += fibonacci(n - 1) + fibonacci(n - 2);
    }
    
}


int main(){
    for(int i=1; i<10; i++){
        std::cout << fibonacci(i) << std::endl;
    }


    return 0;
}