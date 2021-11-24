// Fat Gram Calculator
// Sam Mallet 6/17/2021

#include <iostream>
using namespace std;

int main()
{
    int calories, fat;

    cout << "Enter Calories then Fat in grams" << endl;
    cin >> calories;
    cin >> fat;

    double fat_percent = (fat * 9.0) / calories;

    cout << "Percentage of caloies from fat: " << fat_percent << " (" << (fat_percent * 100) << "%)" << endl;

    if (fat_percent < .3)
        cout << "This food is low in fat";
}