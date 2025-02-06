#include <iostream>

int main(){

    int mat[][3] = {{1, 2, 3},
                    {4, 5, 6},
                    {7, 8, 9}};

    int rows = sizeof(mat)/sizeof(mat[0]);
    int columns = sizeof(mat[0])/sizeof(mat[0][0]);


    for(int i=0; i<rows; i++){
        for(int j=0; j<columns; j++){
            std::cout << mat[i][j] << '\n';
        }
    }


    return 0;
}