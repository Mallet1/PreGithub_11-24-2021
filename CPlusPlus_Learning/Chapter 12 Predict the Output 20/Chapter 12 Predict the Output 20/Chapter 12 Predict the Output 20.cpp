// Chapter 12 Predict the Output 20
// Sam Mallet 7/18/2021

#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    string s(5, 'a');
    s.append(3, 'b');
    s.insert(6, "xyz");
    cout << s;
    return 0;
}