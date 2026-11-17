#include <iostream>

struct Student
{
    int roll_no;
    std::string name;
    float marks;
};

int main()
{
    Student s1;
    s1.roll_no = 1;
    s1.name = "Alice";
    s1.marks = 85.5;

    std::cout << "Roll No: " << s1.roll_no << std::endl;
    std::cout << "Name: " << s1.name << std::endl;
    std::cout << "Marks: " << s1.marks << std::endl;

    return 0;
}