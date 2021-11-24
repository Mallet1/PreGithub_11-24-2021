// Pie a la Mode
// Sam Mallet 7/10/2021

#include <iostream>

using namespace std;

int getMode(int[], int);
string getMode(string[], int);
double getMean(int[], int);
void selectionSort(int[], int);
void selectionSort(string[], int);
void swap(int& , int&);

int main()
{
    const int SIZE = 30;
    int pieces[SIZE];
    string favs[SIZE];

    for (int i = 0; i < SIZE; i++)
    {
        cout << "Person " << i + 1 << ", enter your favorite type of pie (apple, pumpkin, or pecan): ";
        cin >> favs[i];

        while (favs[i] != "apple" && favs[i] != "pumpkin" && favs[i] != "pecan")
        {
            cout << "That is not one of the options (apple, pumpkin, and pecan): Try again: ";
            cin >> favs[i];
        }

        cout << "Person " << i + 1 << ", enter the amount of pieces of pie you eat in a year: ";
        cin >> pieces[i];

        while (pieces[i] < 0)
        {
            cout << "Pieces can not be negative. Try again: ";
            cin >> pieces[i];
        }
    }

    selectionSort(pieces, SIZE);
    selectionSort(favs, SIZE);

    cout << endl << "Most people out of this group eat " << getMode(pieces, SIZE) << " pieces of pie per year. The average amount of pie eaten is " << getMean(pieces, SIZE) << " pieces." << endl;
    cout << "The most preferred pie in this group are " << getMode(favs, SIZE) << " pies." << endl;
}


int getMode(int array[], const int size)
{
    int max_occurences = 1;
    int mode = 0;
    int count = 1;
    for (int i = 1; i <= size; i++)
    {
        if (array[i] == array[i - 1])
            count++;
        else
            count = 1;

        if (count > max_occurences)
        {
            max_occurences = count;
            mode = array[i];
        }
    }
    return mode;
}


string getMode(string array[], const int size)
{
    int max_occurences = 1;
    string mode = "";
    int count = 1;
    for (int i = 1; i <= size; i++)
    {
        if (array[i] == array[i - 1])
            count++;
        else
            count = 1;

        if (count > max_occurences)
        {
            max_occurences = count;
            mode = array[i];
        }
    }
    return mode;
}


double getMean(int array[], int size)
{
    double sum = 0;

    for (int i = 0; i < size; i++)
        sum += *(array + i);

    return sum / size;
}


void selectionSort(int array[], int size)
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


void selectionSort(string array[], int size)
{
    string minValue;
    int minIndex;

    for (int start = 0; start < (size - 1); start++)
    {
        minIndex = start;
        minValue = array[start];
        for (int index = start + 1; index < size; index++)
        {
            if (array[index] < minValue)
            {
                minValue = array[index];
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