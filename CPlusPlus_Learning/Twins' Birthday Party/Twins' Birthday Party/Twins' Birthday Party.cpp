// Twins' Birthday Party
// Sam Mallet 7/4/2021

#include <iostream>
#include <vector>
#include <array>

using namespace std;

class GoodieBag
{
public:
    string name;
    string cookie;
    string vehicle;

    GoodieBag()
    {
        name = "";
        cookie = "";
        vehicle = "";
    }

    GoodieBag(string n)
    {
        name = n;
        cookie = "";
        vehicle = "";
    }

    void display_bag()
    {
        cout << name << "'s bag contains a " << vehicle << " and a " << cookie << " cookie." << endl;
    }

    void no_vehicle_display()
    {
        cout << name << "'s bag contains a " << cookie << " cookie." << endl;
    }
};

void add_vehicles(vector <GoodieBag>&, string array[4][4]);
void add_cookies(vector <GoodieBag>&, string array[2][2][4]);

int main()
{
    string kids[12] = { "LaRhonda", "Jamil", "John", "Maria",
                        "Ivy", "Xavier", "Stevie", "Anna",
                        "Isabella", "Marquis", "Michelle", "Jerome"};

    string vehicles[4][4] = { {"White Van", "Green Truck", "Blue SUV", "Red Racecar"},
                            {"Grey Car", "Cube Car", "Black car", "Blue Truck"},
                            {"Plane", "Black Truck", "Yellow Truck", "Blue Jeep"},
                            {"Yellow Racecar", "Red Truck", "Red Car", "White Jeep"} };

    string cookies[2][2][4] = { {{"GingerBread_Man","GingerBread_Man","GingerBread_Man","GingerBread_Man"},{"GingerBread_Man","GingerBread_Man","GingerBread_Man","GingerBread_Man"}},
                                {{"GingerBread_Man","GingerBread_Man","GingerBread_Man","GingerBread_Man"},{"GingerBread_Man","GingerBread_Man","GingerBread_Man","GingerBread_Man"}} };

    vector<GoodieBag> bags;

    //cout << sizeof(kids) / sizeof(kids[0]) << endl;

    // make blank bags
    for (int k = 0; k < sizeof(kids) / sizeof(kids[0]); k++)
    {
        bags.push_back(GoodieBag());
    }

    // add kids names
    for (int i = 0; i < bags.size(); i++)
    {
        bags[i].name = kids[i];
        kids[i] = "";
    }

    // add vehicle names
    add_vehicles(bags, vehicles);

    // add cookies
    add_cookies(bags, cookies);

    bags.push_back(GoodieBag("Lakeisha"));
    bags.push_back(GoodieBag("Taneisha"));

    add_vehicles(bags, vehicles);

    bags.push_back(GoodieBag("Auntie"));
    bags.push_back(GoodieBag("Uncle"));

    add_cookies(bags, cookies);

    for (int i = 0; i < bags.size(); i++)
    {
        if (bags[i].vehicle == "")
            bags[i].no_vehicle_display();
        else
            bags[i].display_bag();
    }

    cout << "Auntie Your cold beverage is a Sprite!" << endl;
    cout << "Uncle Your cold beverage is a Coke!" << endl;

    cout << endl << "Happy birthday LaKeisha and Taneisha!" << endl;
}

void add_vehicles(vector <GoodieBag>& bags, string vehicles[4][4])
{
    for (int i = 0; i < bags.size(); i++)
    {
        bool go_on = false;

        for (int row = 0; row < 4; row++)
        {
            for (int col = 0; col < 4; col++)
            {
                if (bags[i].vehicle == "")
                {
                    bags[i].vehicle = vehicles[row][col];
                    vehicles[row][col] = "";
                    go_on = true;
                }
                if (go_on == true)
                    continue;
            }
            if (go_on == true)
                continue;
        }
    }
}

void add_cookies(vector <GoodieBag>& bags, string cookies[2][2][4])
{
    for (int i = 0; i < bags.size(); i++)
    {
        bool go_on = false;
        for (int arr = 0; arr < 2; arr++)
        {
            for (int row = 0; row < 2; row++)
            {
                for (int col = 0; col < 4; col++)
                {
                    if (bags[i].cookie == "")
                    {
                        bags[i].cookie = cookies[arr][row][col];
                        cookies[arr][row][col] = "";
                        go_on = true;
                    }
                    if (go_on == true)
                        continue;
                }
                if (go_on == true)
                    continue;
            }
            if (go_on == true)
                continue;
        }
    }
}