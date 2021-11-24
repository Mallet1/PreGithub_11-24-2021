// Test Scores One
// Sam Mallet 7/10/2021

#include <iostream>

using namespace std;

void selectionSort(double[], int);
void swap(int&, int&);
double getAverage(double[], int);

int main()
{
    int* num_of_scores;
    double* scores;
    num_of_scores = new int;
    cout << "Enter the number of scores: ";
    cin >> *num_of_scores;

    while (*num_of_scores < 0)
    {
        cout << "The number of scores cannot be below zero. Try again: ";
        cin >> *num_of_scores;
    }

    scores = new double[*num_of_scores];

    for (int i = 0; i < *num_of_scores; i++)
    {
        cout << "Enter score " << i + 1 << ": ";
        cin >> *(scores + i);

        while (*(scores + i) < 0 or *(scores + i) > 100)
        {
            cout << "Scores cannot be below zero or greater than 100. Try again: ";
            cin >> *(scores + i);
        }
    }

    selectionSort(scores, *num_of_scores);

    cout << endl << "Sorted Scores:" << endl;

    for (int i = 0; i < *num_of_scores; i++)
    {
        cout << endl << *(scores + i);
    }

    cout << endl << endl << "Average:" << endl << "%" << getAverage(scores, *num_of_scores) << endl;
}

void selectionSort(double array[], int size)
{
    int minValue;
    int minIndex;

    for (int start = 0; start < (size - 1); start++)
    {
        minIndex = start;
        minValue = *(array + start);
        for (int index = start + 1; index < size; index++)
        {
            if (*(array + index) < minValue)
            {
                minValue = *(array + index);
                minIndex = index;
            }
        }
        swap(array[minIndex], array[start]);
    }
}

void swap(int& a, int& b)
{
    int temp = a;
    a = b;
    b = temp;
}


double getAverage(double array[], int num_of_scores)
{
    double sum = 0;

    for (int i = 0; i < num_of_scores; i++)
        sum += *(array + i);

    return sum / num_of_scores;
}