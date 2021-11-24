// Rotate Left
// Sam Mallet 7/24/2021

#include <iostream>
#include <vector>


using namespace std;

template<class T>
void rotateLeft(vector <T>&);

template<class T>
void output(vector <T>);

int main()
{
    vector<int> int_vector = { 1, 3, 5, 7 };
    cout << "Original vector: ";
    output(int_vector);

    for (int i = 0; i < 3; i++)
    {
        rotateLeft(int_vector);
        output(int_vector);
    }
    cout << endl;

    vector<char> char_vector = { 'a', 'b', 'c', 'd', 'e', };
    cout << "Original vector: ";
    output(char_vector);

    for (int i = 0; i < 4; i++)
    {
        rotateLeft(char_vector);
        output(char_vector);
    }
    cout << endl;

    vector<double> double_vector = { 1.1, 3.3, 5.5, 7.7 };
    cout << "Original vector: ";
    output(double_vector);

    for (int i = 0; i < 3; i++)
    {
        rotateLeft(double_vector);
        output(double_vector);
    }
    cout << endl;

    vector<string> string_vector = { "Pecan", "Apple", "Pumpkin", "Cherry"};
    cout << "Original vector: ";
    output(string_vector);

    for (int i = 0; i < 3; i++)
    {
        rotateLeft(string_vector);
        output(string_vector);
    }
    cout << endl;
}

template<class T>
void rotateLeft(vector <T>& v)
{
    T temp = v[0];
    v.erase(v.begin());
    v.push_back(temp);
}

template<class T>
void output(vector <T> v)
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}