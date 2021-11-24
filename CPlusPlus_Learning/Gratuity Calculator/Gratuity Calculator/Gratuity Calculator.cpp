// Gratuity Calculator
// Sam Mallet 7/3/2021

#include <iostream>
#include <iomanip>
using namespace std;

class Tips
{   private:
        double taxRate;

    public:
        Tips()
        {
            taxRate = .085;
        }

        Tips(double r)
        {
            taxRate = r;
        }
        
        double computeTip(double bill, double tip)
        {
            double noTax = bill * tip;
            return noTax + (noTax * taxRate);
        }
};

int main()
{
    int again;
    do
    {
        Tips tip;
        double tax, bill, tipRate;

        cout << "Enter the taxRate as a percentage (Enter 0 for the default tax rate): ";
        cin >> tax;

        while (tax < 0 || tax > 100)
        {
            cout << "Error: Your tax rate must be between 0 and 100. Please try again: ";
            cin >> tax;
        }

        cout << "Enter the untaxed, untipped bill: ";
        cin >> bill;

        while (bill <= 0)
        {
            cout << "Error: Your bill must be greater than 0. Please try again: ";
            cin >> bill;
        }

        cout << "Enter your tip rate as a percentage: ";
        cin >> tipRate;

        while (tipRate < 0 || tipRate > 100)
        {
            cout << "Error: Your tip rate must be between 0 and 100. Please try again: ";
            cin >> tipRate;
        }

        while (tipRate < 15)
        {
            cout << "This tip rate is less than 15%. The wait staff in US restaurants don't earn minimum wage, and need a better tip than that." << endl;
            cout << "Please enter another tip that is 15% or greater: ";
            cin >> tipRate;
        }

        if (tipRate >= 20)
            cout << "Thank you for your generosity." << endl;

        tipRate *= .01;
        tax *= .01;

        if (tax != 0)
            tip = Tips(tax);
        else
            tax = .085;

        double taxedTip = tip.computeTip(bill, tipRate);
        double taxAmount = ((bill * tipRate) + bill) * tax;

        cout << fixed << setprecision(2) << "Taxed tip: $" << taxedTip << endl;
        cout << fixed << setprecision(2) << "tip and bill Tax: $" << taxAmount << endl;
        cout << fixed << setprecision(2) << "Total bill: $" << (bill + (bill * tax) + taxedTip) << endl;
        cout << fixed << setprecision(2) << "Your untaxed tip amount is $" << (bill * tipRate) << endl;

        cout << "Enter 0 to quit and 1 to continue: ";
        cin >> again;
    } while (again != 0);
}