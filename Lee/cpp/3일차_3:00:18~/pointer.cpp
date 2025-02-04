#include <iostream>

int main(){

    std::string name = "MovingJu";

    std::string *p_name = &name;

    std::cout << p_name << ", " << *p_name << '\n';

    int nums[10];
    std::fill(nums, nums + 10, 0);

    int *p_nums = nums;

    std::cout << p_nums << ", " << *p_nums << '\n';
    

    return 0;
}