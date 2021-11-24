// How many Calories?
// Sam Mallet 6/15/2021

#include <iostream>
using namespace std;

int main()
{
    int cookies, calories;

    cout << "How many cookies did you eat? ";
    cin >> cookies;

    calories = cookies * 80;
    cout << "You ate " << calories << " calories";
}