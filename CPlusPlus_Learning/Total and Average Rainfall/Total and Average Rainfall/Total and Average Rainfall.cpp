// Total and Average Rainfall
// Sam Mallet 6/26/2021

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    string month_start, month_end;
    double rain;
    double total_precip = 0;
    int total_rain = 0;
    ifstream inFile("C:\\Users\\Sam Mallet\\source\\repos\\rainfall.txt");
    inFile >> month_start >> month_end;
    
    while (inFile >> rain)
    {
        total_precip += rain;
        total_rain++;
    }

    cout << fixed << setprecision(2) << "During the months of " << month_start << "-" << month_end <<
        ", the total rainfall was " << total_precip <<
        " inches and the average monthly rainfall was " <<
        (total_precip / total_rain) << " inches" << endl;
}