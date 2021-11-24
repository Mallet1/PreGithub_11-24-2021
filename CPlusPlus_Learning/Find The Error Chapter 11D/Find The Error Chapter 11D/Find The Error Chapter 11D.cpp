// Find The Error Chapter 11D
// Sam Mallet 7/17/2021

#include <iostream>

using namespace std;

class Box
{
private:
	double width;
	double length;
	double height;
public:
	Box(double w, double l, double h)
	{
		width = w; length = l; height = h;
	}

	// Overloaded prefix ++ operator
	void operator++()
	{
		++width; ++length;
	}

	// Overloaded postfix ++ operator
	void operator++(int)
	{
		width++; length++;
	}

	double get_width()
	{
		return width;
	}

	double get_length()
	{
		return length;
	}
};

int main()
{
	Box new_box(2, 3, 2);

	cout << "Width: " << new_box.get_width() << endl;
	cout << "Length: " << new_box.get_length() << endl << endl;

	new_box++;

	cout << "Width: " << new_box.get_width() << endl;
	cout << "Length: " << new_box.get_length() << endl;
}