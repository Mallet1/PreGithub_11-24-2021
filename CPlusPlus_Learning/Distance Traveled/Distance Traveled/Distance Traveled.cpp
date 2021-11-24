// Distance Traveled
// Sam Mallet 6/26/2021

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int speed, time;
    cout << "Enter the speed of your vehicle in miles per hour: ";
    cin >> speed;

    cout << "Enter your hours traveled: ";
    cin >> time;

    cout << endl << "Hour" << setw(25) << "Miles Traveled" << endl;
    cout << setfill('-') << setw(30) << "" << endl;
    for (int i = 1; i <= time; i++)
    {
        cout << " " << setfill(' ') << i << setw(20) << (i * speed) << endl;
    }
}