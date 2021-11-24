// Day of the Year Modification
// Sam Mallet 7/15/2021

#include <iostream>
#include <stdlib.h>

using namespace std;

class DayOfYear
{
private:
    int day;
    int month_day;

    static string months[12];
    static int days[];

public:
    DayOfYear(int day)
    {
        this->day = day;
    }

    DayOfYear(string month, int day)
    {
        month_day = day;

        for (int i = 0; i < 12; i++)
        {
            if (month == months[i])
                day += days[i];
        }

        this->day = day;

        bool isMonth = false;

        for (int i = 0; i < 12; i++)
        {
            if (month == months[i] && (month_day < 1 || month_day > days[i + 1] - days[i]))
            {
                cout << "Error: day must be between 1 and " << days[i + 1] - days[i] << "." << endl;
                exit(EXIT_FAILURE);
            }

            if (month == months[i])
                isMonth = true;
        }

        if (isMonth == false)
        {
            cout << "Error: Invalid month, must be either January, February, March, April, May, June, July, August, September, October, November, or December" << endl;
            exit(EXIT_FAILURE);
        }
    }

    void print_day()
    {
        for (int i = 0; i < 12; i++)
        {
            if (day > days[i] && day <= days[i + 1])
            {
                cout << months[i] << " " << (day - days[i]);
                break;
            }
        }
    }

    int get_day()
    {
        return day;
    }

    void operator++() 
    {
        if (day == 365)
            day = 1;
        else
            day++;
    }
    void operator--()
    {
        if (day == 1)
            day = 365;
        else
            day--;
    }
    void operator++(int r)
    {
        if (day == 365)
            day = 1;
        else
            ++day;
    }
    void operator--(int r)
    {
        if (day == 1)
            day = 365;
        else
            --day;
    }
};

string DayOfYear::months[12] = { "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" };
int DayOfYear::days[] = { 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365 };

int main()
{
    string month;
    int day;

    cout << "Enter a month: ";
    cin >> month;

    cout << "Enter a day of the month: ";
    cin >> day;

    DayOfYear convert_date(month, day);

    cout << "Day of year = " << convert_date.get_day() << endl;

    --convert_date;

    cout << "Prefix day decrement = " << convert_date.get_day() << endl;
}