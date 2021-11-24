// Day of the Year
// Sam Mallet 7/15/2021

#include <iostream>

using namespace std;

class DayOfYear
{
private:
    int day;

    static string months[];
    static int days[];

public:
    DayOfYear(int day)
    {
        this->day = day;
    }

    void print()
    {
        for (int i = 0; i < 13; i++)
        {
            if (day > days[i] && day <= days[i + 1])
            {
                cout << months[i] << " " << (day - days[i]);
                break;
            }
        }
    }
};

string DayOfYear::months[] = { "January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" };
int DayOfYear::days[] = { 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365 };

int main()
{
    int day;

    cout << "Enter a day of the year 1-365: ";
    cin >> day;

    while (day < 1 || day > 365)
    {
        cout << "Error: day must be between 1 and 365, try again. ";
        cin >> day;
    }

    DayOfYear convert_day(day);

    convert_day.print();
}