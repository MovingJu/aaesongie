#include <iostream>
#include <vector>

// typedef std::vector<std::pair<std::string, int>> pairlist_t;
// 너무 긴 변수명을 대체, 보통 _t 를 붙여줌.
// typedef 보단 using이 낫대.

typedef std::string str_t;

using integer = int;
using ft = double;

int main(){

    str_t t = "hellow world!";

    std::cout << t << std::endl;



    return 0;
}