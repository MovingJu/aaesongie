#include <iostream>

namespace first{
    int x = 1;
}

namespace second{
    int x = 2;
}

int main(){
    // using namespace std;      너무 많은 내용을 한번에 import해오는 꼴.
    using std::cout;
    using std::endl;
    using namespace first;

    cout << x << endl;

    return 0;
}