// Baseball Champions
// Sam Mallet 7/4/2021

#include <iostream>
#include <fstream>
#include <vector>
#include <cctype>
#include <string>

using namespace std;

vector<string> getFileContents(string);

int main()
{
    string teamInput;
    bool isTeam = false;
    int winSum = 0;

    vector<string> teams = getFileContents("C:\\Users\\Sam Mallet\\source\\repos\\Teams.txt");
    vector<string> winners = getFileContents("C:\\Users\\Sam Mallet\\source\\repos\\WorldSeriesWinners.txt");

    cout << "Teams:" << endl;
    for (int i = 0; i < teams.size(); i++)
        cout << teams[i] << endl;
    
    cout << "Enter the name of one of the teams: ";
    getline(cin, teamInput);

    do
    {
        for (int i = 0; i < teams.size(); i++)
        {
            if (teams[i] == teamInput)
                isTeam = true;
        }
        if (!isTeam)
        {
            cout << "Error: That is not a team. Please enter a team: ";
            getline(cin, teamInput);
        }
    } while (!isTeam);

    for (int i = 0; i < winners.size(); i++)
    {
        if (winners[i] == teamInput)
            winSum++;
    }

    cout << "That team has won " << winSum << " games between 1950 and 2014." << endl;
}

vector<string> getFileContents(string directory)
{
    string line;
    vector<string> contents;
    ifstream file;
    file.open(directory);

    if (!file)
    {
        cout << "Error opening file" << endl;
    }
    else
    {
        while (getline(file, line))
            contents.push_back(line);

        file.close();
    }
    return contents;
}