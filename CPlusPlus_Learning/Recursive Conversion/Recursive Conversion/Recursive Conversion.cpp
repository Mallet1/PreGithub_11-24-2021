// Recursive Conversion
// Sam Mallet 7/23/2021

#include <iostream>

using namespace std;

void original(int);
void sign(int);

int main()
{
    cout << "Original: " << endl;
    original(5);
    cout << endl << "Recursion: " << endl;
    sign(5);
}

void original(int n)
{
    while (n > 0)
    {
        cout << "No Parking\n";
        n--;
    }
}

void sign(int n)
{
    if (n > 0)
    {
        cout << "No Parking\n";
        sign(n - 1);
    }
    else
        cout << "";
}