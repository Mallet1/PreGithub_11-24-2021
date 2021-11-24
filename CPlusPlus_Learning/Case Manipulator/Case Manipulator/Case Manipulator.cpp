// Case Manipulator
// Sam Mallet 7/18/2021

#include <iostream>
#include <cstring>
#include <cctype>

using namespace std;

char* upper(char*);
char* lower(char*);
char* flip(char*);

int main()
{
    const int SIZE = 10;
    char str[SIZE];
    cout << "Enter a sentence or word: ";
    cin.getline(str, SIZE);

    cout << "Flip: " << flip(str) << endl;
    cout << "Upper: " << upper(str) << endl;
    cout << "Lower: " << lower(str) << endl;
}

char* upper(char* str)
{
    int len = strlen(str);

    for (int i = 0; i < len; i++)
        str[i] = toupper(str[i]);

    return str;
}

char* lower(char* str)
{
    int len = strlen(str);

    for (int i = 0; i < len; i++)
        str[i] = tolower(str[i]);

    return str;
}

char* flip(char* str)
{
    int len = strlen(str);

    for (int i = 0; i < len; i++)
        if (isupper(str[i]))
            str[i] = tolower(str[i]);
        else
            str[i] = toupper(str[i]);

    return str;
}