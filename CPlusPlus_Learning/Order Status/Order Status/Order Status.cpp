// Order Status
// Sam Mallet 6/27/2021

#include <iostream>
using namespace std;

void getInfo(int&, int&, double&);
void displayInfo(int, int, double);

int main(int&, int&, double&)
{
	int ordered_spools, spools_in_stock, again;
	double ship_charges;
	
	do
	{
		getInfo(ordered_spools, spools_in_stock, ship_charges);
		displayInfo(ordered_spools, spools_in_stock, ship_charges);

		cout << endl << "Enter anything to contine and 0 to quit: ";
		cin >> again;
	} while (again != 0);
}

void getInfo(int& ordered, int& stock, double& charges)
{
	cout << "Enter the number of spools ordered: ";
	cin >> ordered;

	cout << "Enter the number of spools in stock: ";
	cin >> stock;

	cout << "Enter any special shipping and handling charges above the regular $10 rate): ";
	cin >> charges;
}

void displayInfo(int ordered, int stock, double charges = 10.0)
{
	cout << "The number of ordered spools ready to ship from current stock: " << stock << endl;
	if (ordered > stock)
		cout << "The number of ordered spools on backorder: " << (ordered - stock) << endl;

	cout << "Total selling price of the portion ready to ship: $" << (stock * 100) << endl;
	cout << "Total shipping and handling charges on the portion ready to ship: $" << (stock * charges) << endl;
	cout << "Total of the order ready to ship: $" << ((stock * 100) + (stock * charges)) << endl;
}