// Recursive Multiplication
// Sam Mallet 7/23/2021

#include <iostream>

using namespace std;

int mult(int, int);

int main()
{
    int x;
    int y;

    try
    {
        cout << "Enter two positive integers to be multiplied recursively." << endl;
        cout << "Integer 1: ";
        cin >> x;

        if (x < 0) throw string("Bad argument!");

        cout << "Integer 2: ";
        cin >> y;

        if (y < 0) throw string("Bad argument!");
        
        cout << x << " * " << y << " = " << mult(x, y) << endl;
    }
    catch (string str)
    {
        cout << str << endl;
    }
}

int mult(int x, int y)
{
    if (x > 0)
        return y + mult(x - 1, y);
    else
        return 0;
}