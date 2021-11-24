// Lottery Winners
// Sam Mallet 7/10/2021

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int tickets[10] = {13579, 26791, 26792, 33445, 55555, 62483, 77777, 79422, 85647, 93121};
    int winner;
    bool won = false;

    cout << "Enter the winning lottery number (five digits): ";
    cin >> winner;
    int winner_size = trunc(log10(winner)) + 1;

    while (winner_size > 5 or winner_size < 5)
    {
        cout << "The winning number must have exactly five digits. Try again: ";
        cin >> winner;

        winner_size = trunc(log10(winner)) + 1;
    }

    for (int i = 0; i < 10; i++)
    {
        if (tickets[i] == winner)
        {
            won = true;
            cout << "Congradulations you won the lottery!";
            break;
        }
    }

    if (won == false)
        cout << "Sorry you did not win the lottery.";
}