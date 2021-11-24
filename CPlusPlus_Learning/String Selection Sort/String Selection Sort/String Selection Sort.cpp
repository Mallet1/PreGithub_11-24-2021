// String Selection Sort
// Sam Mallet 7/10/2021

#include <iostream>

using namespace std;

void selectionSort(string[], int);
void swap(int&, int&);

int main()
{
    int const SIZE = 20;

    string name[SIZE] = {"Collins, Bill", "Smith, Bart", "Michalski, Joe", "Griffin, Jim", "Sanchez, Manny", 
                        "Rubin, Sarah", "Taylor, Tyrone", "Johnson, Jill", "Allison, Jeff", "Moreno, Juan",
                        "Wolfe, Bill", "Whitman, Jean", "Moretti, Bella", "Wu, Hong", "Patel, Renee",
                        "Harrison, Rose", "Smith, Cathy", "Conroy, Pat", "Kelly, Sean", "Holland, Beth"};

    cout << "Original array:" << endl << endl;
    for (int i = 0; i < SIZE; i++)
        cout << name[i] << endl;
    cout << endl;

    selectionSort(name, SIZE);

    cout << "Sorted array:" << endl << endl;
    for (int i = 0; i < SIZE; i++)
        cout << name[i] << endl;
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