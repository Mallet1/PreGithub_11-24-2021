// Find The Error Chapter 11
// Sam Mallet 7/17/2021

#include <iostream>

using namespace std;


class Box
{
private:
    double width;
    double length;
    double height;
public:
    Box(double w, double l, double h)
    {
        width = w; length = l; height = h;
    }

    Box(const Box &b) // Copy constructor
    {
        width = b.width;
        length = b.length;
        height = b.height;
    }

    void print()
    {
        cout << width << " " << length << " " << height << endl;
    }
};

int main()
{
    Box first_box(10, 8, 4);

    Box second_box(first_box);

    second_box.print();
}