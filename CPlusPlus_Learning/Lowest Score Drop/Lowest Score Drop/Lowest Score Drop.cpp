// Lowest Score Drop
// Sam Mallet 6/27/2021

#include <iostream>
using namespace std;

void getScore(int&);
void calcAverage(int, int, int, int, int, int);
int findLowest(int, int, int, int, int, int);

int main()
{
    int s1, s2, s3, s4, s5, s6;

    cout << "Enter you five test scores below to calculate the average after exempting your lowest:" << endl;

    getScore(s1);
    getScore(s2);
    getScore(s3);
    getScore(s4);
    getScore(s5);
    getScore(s6);

    calcAverage(s1, s2, s3, s4, s5, s6);

}

void getScore(int& score)
{
    cout << "Enter your score: ";
    cin >> score;
    while (score > 100 || score < 0)
    {
        cout << "Score must be between 0 and 100 (inclusive). Try again: ";
        cin >> score;
    }
}

void calcAverage(int s1, int s2, int s3, int s4, int s5, int s6)
{
    double average = (s1 + s2 + s3 + s4 + s5 + s6 - findLowest(s1, s2, s3, s4, s5, s6)) / 5.0;
    cout << "the average of your five scores minus the lowest is " << average;
}

int findLowest(int s1, int s2, int s3, int s4, int s5, int s6)
{
    if (s1 < s2 && s1 < s3 && s1 < s4 && s1 < s5 && s1 < s6)
        return s1;
    else if (s2 < s1 && s2 < s3 && s2 < s4 && s2 < s5 && s2 < s6)
        return s2;
    else if (s3 < s2 && s3 < s1 && s3 < s4 && s3 < s5 && s3 < s6)
        return s3;
    else if (s4 < s2 && s4 < s3 && s4 < s1 && s4 < s5 && s4 < s6)
        return s4;
    else if (s5 < s2 && s5 < s3 && s5 < s1 && s5 < s6 && s5 < s4)
        return s5;
    else
        return s6;
}