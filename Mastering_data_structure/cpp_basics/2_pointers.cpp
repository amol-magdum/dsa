#include <iostream>

int main()
{
    int a=10;
    int *p;
    p=&a;
    std::cout << a << std::endl;
    std::cout << *p << std::endl;
    
    
    int A[5] = {2,4,6,8,10}; /// created in stack
    int *q;
    q=A; //or q=&A[0]
    std::cout << A << std::endl;
    std::cout << *q << std::endl;
    
    for (int i=0;i<5;i++)
    std::cout << q[i] << std::endl;
    
    int *r;
    r=new int[5]; // array inside heap
    
    r[0]=1; r[1]=3; r[2]=5; r[3]=7; r[4]=9;
    for (int i = 0; i < 5; i++) {
        std::cout << r[i] << std::endl;
    }
    
    delete [] r;
    return 0;
}
