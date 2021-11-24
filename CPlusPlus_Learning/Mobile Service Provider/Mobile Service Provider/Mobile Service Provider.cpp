// Mobile Service Provider
// Sam Mallet 6/17/2021

#include <iostream>
using namespace std;

int main()
{
    const double A_MONTHLY = 39.99;
    const double B_MONTHLY = 59.99;
    const double planC = 79.99;
    const int A_GIGABYTES = 2;
    const int B_GIGABYTES = 8;
    const int additional_costs = 8;
    char choice;
    string name;
    double gigabytes;
    
    cout << "Enter you name: ";
    cin >> name;

    cout << "Plan A: For $39.99 per month, 2 gigabytes are provided. Additional usage costs $8.00 per giga byte." << endl;
    cout << "Plan B: For $59.99 per month, 8 gigabytes are provided. Additional usage costs $8.00 per giga byte." << endl;
    cout << "Plan C: For $79.99 per month, unlimited data is provided." << endl;
    cout << "Enter your plan (A, B, or C): ";
    cin >> choice;

    cout << "Enter how many gigabytes you used this month: ";
    cin >> gigabytes;

    double planA = A_MONTHLY;
    if (gigabytes > A_GIGABYTES)
        planA += additional_costs * (gigabytes - A_GIGABYTES);

    double planB = B_MONTHLY;
    if (gigabytes > B_GIGABYTES)
        planB += additional_costs * (gigabytes - B_GIGABYTES);

    switch (choice)
    {
        case 'A': cout << "Hi " << name << "! You purchased plan A and owe " << planA << " this month using " << gigabytes << " gigabytes of data." << endl;
            if (planB < planA && planB < planC)
                cout << "You could have saved $" << (double)(planA - planB) << " if you switched to plan B";
            else if (planC < planA && planC < planB)
                cout << "You could have saved $" << (double)(planA - planC) << " if you switched to plan C";
            break;

        case 'B': cout << "Hi " << name << "! You purchased plan B and owe " << planB << " this month using " << gigabytes << " gigabytes of data." << endl;
            /*if (planA < planB && planA < planC)
                cout << "You could have saved $" << (double)(planB - planA) << " if you switched to plan A";*/
            if (planC < planB/* && planC < planA*/)
                cout << "You could have saved $" << (double)(planB - planC) << " if you switched to plan C";
            break;

        case 'C': cout << "Hi " << name << "! You purchased plan C and owe " << planC << " this month using " << gigabytes << " gigabytes of data." << endl;
            /*if (planA < planC && planA < planB)
                cout << "You could have saved $" << (double)(planC - planA) << " if you switched to plan A";
            else if (planB < planC && planB < planA)
                cout << "You could have saved $" << (double)(planC - planB) << " if you switched to plan B";*/
            break;

        default: cout << "Invalid plan" << endl;
    } // Wasn't sure if I should display the savings with superior plans for all of them
}