// Static Extra Credit
// Sam Mallet 7/8/2021

#include <iostream>
using namespace std;

class someClass  //defining a new class with the this pointer
{
private:
    int nu = 0;
public:
    int setNum(int num) const
    {
        int newnum = 25;
        cout << "This starts by pointing to " << this->nu << endl;
        cout << "The num that got passed in was " << num << endl;
        // this->nu = num;
        num = newnum;
        cout << "And the new value of num is " << num << endl;
        return num;
    }
};  //someClass ends here
// int IntVal::valCount = 0;
class IntVal
{
public:
    intVal(int val = 0);
    { value = val; valCount++ }
    int getVal();
    void setVal(int);

private:
    int value;
    static int valCount();
};
int IntVal::valCount = 0;

int main()
{
    int n = 73;
    /* I want to create an instance of someClass and call it sC*/
    someClass sC;
    /* Now, I want to call setNum and pass it n */
    n = sC.setNum(n);
    cout << "And the new value passed from sC is " << n << endl;
    std::cout << "Hello World!\n";
}