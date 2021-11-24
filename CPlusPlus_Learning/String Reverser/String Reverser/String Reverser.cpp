// String Reverser
// Sam Mallet 7/23/2021

#include <iostream>

using namespace std;

void str_reversed(string);

int main()
{
    string str;

    try
    {
        cout << "Enter a string to be reversed: ";
        cin >> str;

        if (str.length() <= 1)
            throw string("Error: Must have a length greater than one to be reversed");

        cout << "Reversed: ";
        str_reversed(str);
    }
    catch (string x)
    {
        cout << x << endl;
    }
}

void str_reversed(string str)
{
    if (str.length() > 1)
    {
        cout << str.substr(str.length() - 1);
        str_reversed(str.substr(0, str.length()-1));
    }
    else
        cout << str << endl;
}