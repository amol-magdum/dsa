#include <iostream>

int main()
{
    int A[10]; // defined size
    int B[] = {23, 45, 58};    
    A[0]=465465;
    A[1]=1234;
    A[2]=4321;
    std::cout << sizeof(A) << std::endl;
    std::cout << A[1] << std::endl;
    std::cout << A[2] << std::endl;
    printf("%d\n",A[2]);
    printf("Running for loop");
    for(int i=0;i<10;i++)
    {
        std::cout<<A[i]<<std::endl;
    }
    return 0;
}