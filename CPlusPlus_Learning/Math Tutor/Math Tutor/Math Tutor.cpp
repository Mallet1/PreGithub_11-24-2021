// Math Tutor
// Sam Mallet 6/15/2021

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	unsigned seed;

	seed = time(0);
	srand(seed);

	int random1 = rand() % 9 + 1;
	int random2 = rand() % 9 + 1;
	int answer;

	cout << " " << random1 << endl << "+" << random2 << endl;
	cin >> answer;

	if (answer == (random1 + random2))
		cout << answer << " is correct!";
	else
		cout << answer << " is incorrect. The correct answer is " << (random1 + random2);
}