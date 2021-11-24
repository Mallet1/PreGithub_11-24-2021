// Overloaded Hospital
// Sam Mallet 4/27/2021

#include <iostream>
#include <cctype>
using namespace std;

void checkInput(double&);
double calcCharges(double, double, double, double);
double calcCharges(double, double);

int main()
{
    int again = 1;
    while (again != 0)
    {
        int patient_type;
        double days, daily_rate, service_charges, med_charges;

        cout << "If you are an inpatient enter 0. If you are an outpatient enter 1: ";
        cin >> patient_type;

        if (patient_type == 0)
        {
            cout << "Enter the number of days spent in the hospital: ";
            cin >> days;
            checkInput(days);

            cout << "Enter the daily rate: ";
            cin >> daily_rate;
            checkInput(daily_rate);

            cout << "Enter the charges for hospital services (lab tests, etc.): ";
            cin >> service_charges;
            checkInput(service_charges);

            cout << "Enter the hospital medication charges: ";
            cin >> med_charges;
            checkInput(med_charges);

            cout << "The total charges from your hospital visit amounts to $" << calcCharges(days, daily_rate, service_charges, med_charges) << endl << endl;
        }
        else if (patient_type == 1)
        {
            cout << "Enter the charges for hospital services (lab tests, etc.): ";
            cin >> service_charges;
            checkInput(service_charges);

            cout << "Enter the hospital medication charges: ";
            cin >> med_charges;
            checkInput(med_charges);

            cout << "The total charges from your hospital visit amounts to $" << calcCharges(service_charges, med_charges) << endl << endl;
        }
        cout << "Enter 0 to quit or 1 to continue: ";
        cin >> again;
    }
}

void checkInput(double& input)
{
    if (input < 0)
    {
        cout << "This value cannot be below 0: Please re-enter: ";
        cin >> input;
    }
}

double calcCharges(double days, double daily_rate, double service_charges, double med_charges)
{
    return (days * daily_rate) + service_charges + med_charges;
}

double calcCharges(double service_charges, double med_charges)
{
    return service_charges + med_charges;
}