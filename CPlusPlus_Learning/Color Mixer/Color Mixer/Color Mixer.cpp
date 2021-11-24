// Color Mixer
// Sam Mallet 6/17/2021

#include <iostream>
using namespace std;

int main()
{
    string color1, color2;

    cout << "Enter the name of of two primary colors to mix" << endl;
    cin >> color1;
    cin >> color2;

    if ((color1 == "red" && color2 == "blue") || (color1 == "blue" && color2 == "red"))
        cout << endl << "purple";
    else if ((color1 == "red" && color2 == "yellow") || (color1 == "yellow" && color2 == "red"))
        cout << endl << "orange";
    else if ((color1 == "blue" && color2 == "yellow") || (color1 == "yellow" && color2 == "blue"))
        cout << endl << "green";
    else
        cout << "Error: Not a primary color. Primary colors include red, blue, and yellow";
}