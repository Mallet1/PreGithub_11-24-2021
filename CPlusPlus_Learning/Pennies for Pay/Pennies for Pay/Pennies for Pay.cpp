// Pennies for Pay
// Sam Mallet 6/26/2021

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int time = 0;
    double profit = .01;

    cout << "Enter the amount of days you worked this month: ";
    cin >> time;

    while (time < 1 || time > 31)
    {
        cout << endl << "Out of Range: days worked must be betwee 1 and 31, try again.";
        cout << "Enter the amount of days you worked this month: ";
        cin >> time;
    }

    cout << endl << "Day" << setw(25) << "Money Earned" << endl;
    cout << setfill('-') << setw(30) << "" << endl;
    for (int i = 1; i <= time; i++)
    {
        cout << " " << setfill(' ') << i << setw(20);
        cout << fixed << setprecision(2) << "$" << profit << endl;
        profit = profit * 2;
    }
    cout << endl << setprecision(2) << "Total salary for the month: $" << profit / 2;
}