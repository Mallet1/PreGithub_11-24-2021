// Check Writing
// Sam Mallet 7/15/2021

#include <iostream>

using namespace std;

class Numbers
{
private:
    int num;

    static string below_20[];
    static string tens[];

public:
    Numbers(int num)
    {
        this->num = num;
    }
    void print()
    {
        int temp = num;

        if (temp >= 1000)
        {
            cout << below_20[temp / 1000] + " thousand ";
            temp %= 1000;
        }

        if (temp >= 100)
        {
            cout << below_20[temp / 100] + " hundred ";
            temp %= 100;
        }

        if (temp >= 20)
        {
            cout << tens[temp / 10] + " ";
            temp %= 10;
        }

        if (temp < 20 && temp > 0)
            cout << below_20[temp];

        if (temp == 0)
            cout << "zero";

        cout << endl;
    }
};

string Numbers::below_20[] = {"", "one", "two", "three", "four", "five", "six","seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen" ,"eighteen", "nineteen"};
string Numbers::tens[] = {"", "", "twenty","thirty","fourty","fifty", "sixty", "seventy", "eighty", "ninety"};

int main()
{
    int num;

    cout << "Enter a positive number: ";
    cin >> num;

    while (num < 0)
    {
        cout << "Error: the number must be positive, try again. ";
        cin >> num;
    }

    Numbers convert_num(num);

    convert_num.print();
}