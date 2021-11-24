// Moving Inchworm
// Sam Mallet 7/3/2021

#include <iostream>
#include <windows.h>
#include <iomanip>

using namespace std;

int main()
{
    HANDLE screen = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD position;
    position.X = 0;
    position.Y = 0;
    int row = 0;
    int col = 0;
    bool full_up = false;
    bool one_up = false;
    bool full_down = true;
    string prev;

    while (true)
    {
        position.Y = 0;
        position.X++;
        SetConsoleCursorPosition(screen, position);
        cout << setw(13) << "\\/" << endl;
        position.Y = 1;
        SetConsoleCursorPosition(screen, position);
        cout << setw(13) << "OO" << endl;

        if (full_up)
        {
            position.Y = 2;
            SetConsoleCursorPosition(screen, position);
            cout << " ~OOO";
            position.Y = 1;
            position.X ;
            SetConsoleCursorPosition(screen, position);
            cout << "OOO";
            position.X -= 0;
            position.Y = 2;
            SetConsoleCursorPosition(screen, position);
            cout << "OOO";

            full_up = false;
            one_up = true;
            full_down = false;
            prev = "full_up";
        }

        if (one_up)
        {
            position.Y = 2;
            SetConsoleCursorPosition(screen, position);
            cout << "  ~OOO";
            cout << "O";
            position.Y = 1;
            SetConsoleCursorPosition(screen, position);
            cout << setw(9) << "O";
            position.Y = 2;
            SetConsoleCursorPosition(screen, position);
            cout << "O";
            cout << "OOO";

            if (prev == "full_up")
                full_down = true;
            else
                full_up = true;
            one_up = false;

            prev = "one_up";
        }

        if (full_down)
        {
            position.Y = 2;
            SetConsoleCursorPosition(screen, position);
            cout << "   ~OOO";
            cout << "O";
            cout << "O";
            cout << "O";
            cout << "OOO";

            full_up = false;
            one_up = true;
            full_down = false;
            prev = "full_down";
        }
        Sleep(250);
    }
}
