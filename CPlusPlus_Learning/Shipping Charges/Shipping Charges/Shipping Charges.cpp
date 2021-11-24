// Shipping Charges
// Sam Mallet 6/27/2021

#include <iostream>
#include <iomanip>
using namespace std;

double calculateCharge(double weight, int distance);

int main()
{
    int distance;
    double weight;

    while (true)
    {
        cout << "Enter the weight of the package and the distance it is to be shipped" << endl << "Weight (kg): ";
        cin >> weight;
        if (weight <= 0)
            break;
        cout << "Distance (miles): ";
        cin >> distance;

        double shipping_cost = calculateCharge(weight, distance);

        cout << fixed << setprecision(2) << "The shipping cost for a " << weight << "kg package " << distance << " miles away is $" << shipping_cost << endl << endl;
    }
}

double calculateCharge(double weight, int distance)
{
    double rate;

    if (weight <= 2.0)
        rate = 3.1;
    else if (weight <= 6.0)
        rate = 4.2;
    else if (weight <= 10.0)
        rate = 5.3;
    else
        rate = 6.4;

    return ((distance + 499) / 500) * rate;
}