#include <iostream>

struct Rectangle{
    int length;
    int breath;
};

/// pass by value
/// @param r 
void funByValue(struct Rectangle r){
    std::cout << "Length: " << r.length << ", Breath: " << r.breath << std::endl;
};

void funByAddress(struct Rectangle *ptr){
    std::cout << "Length: " << ptr->length << ", Breath: " << ptr->breath << std::endl;
};
int main()
{
    struct Rectangle r = {10,5};
    std::cout << "Length: " << r.length << ", Breath: " << r.breath << std::endl;
    funByValue(r);
    
    struct Rectangle r2 = {20,15};
    struct Rectangle *ptr = &r2;
    std::cout << "Length: " << ptr->length << ", Breath: " << ptr->breath << std::endl;

    funByAddress(&r2); // pass ptr
    return 0;
}