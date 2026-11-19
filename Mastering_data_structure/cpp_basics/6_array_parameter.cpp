// passing array as parameter to function in C++.
// its is passed as pointer to the first element of the array.


#include <iostream>

void fun(int A[ ], int n)
{
    // for(int i=0;i<n;i++)
    // std::cout << A[i] << std::endl;
    A[4]=20; // change original value as its pointer
}

int main()
{
    int A[]={2,4,6,8,10};
    int n=5;
    fun(A,n);
    for (int i:A) {
        /* code */
        std::cout << i << std::endl;
    }
    return 0;
    
}