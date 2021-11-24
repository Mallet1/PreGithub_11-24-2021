// Random Number Guessing Game
// Sam Mallet 6/26/2021

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    unsigned seed = time(0);
    srand(seed);
    int randNum = rand() % 100 + 1;
    int guess;

    cout << "I am thinking of a number 1-100. Enter your guess here: ";
    cin >> guess;

    while (guess != randNum)
    {
        if (guess < randNum) 
        {
            cout << "Too low. Try again. ";
            cin >> guess;
        }
        else if (guess > randNum)
        {
            cout << "Too high. Try again. ";
            cin >> guess;
        }
    }
    cout << "Congratulations. You figured out my number.";
}