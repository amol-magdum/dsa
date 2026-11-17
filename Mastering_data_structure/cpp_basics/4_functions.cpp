#include <iostream>

int add(int a, int b)
{
    return a + b;
}

int main()
{
    int result = add(5, 3);
    std::cout << "The sum is: " << result << std::endl;
    return 0;
}