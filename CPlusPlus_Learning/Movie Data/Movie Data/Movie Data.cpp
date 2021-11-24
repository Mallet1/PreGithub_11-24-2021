// Movie Data
// Sam Mallet 7/3/2021

#include <iostream>
using namespace std;

struct MovieData
{
    string title,
        director,
        release_year,
        running_time;

    MovieData(string t, string d, string y, string r)
    {
        title = t;
        director = d;
        release_year = y;
        running_time = r;
    }
};

void display_data(MovieData);

int main()
{
    MovieData oceans8("Oceans 8", "Gary Ross", "2018", "1:51");
    MovieData jurassic_world("Jurassic World: Fallen Kingdom", "Colin Trevorrow", "2015", "2:05");
    MovieData deadpool("Deadpool 2", "David Leitch", "2018", "2:14");
    MovieData star_wars("Solo: A Star Wars Story", "Ron Howard", "2018", "2:15");
    MovieData incredibles("Incredibles 2", "Brad Bird", "2018", "2:05");

    display_data(oceans8);
    display_data(jurassic_world);
    display_data(deadpool);
    display_data(star_wars);
    display_data(incredibles);
}

void display_data(MovieData data)
{
    cout << "Title: " << data.title << endl;
    cout << "Director: " << data.director << endl;
    cout << "Release Year: " << data.release_year << endl;
    cout << "Running Time: " << data.running_time << endl << endl;
}