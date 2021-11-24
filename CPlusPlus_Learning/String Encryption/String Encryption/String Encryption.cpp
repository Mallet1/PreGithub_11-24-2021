// String Encryption
// Sam Mallet 7/18/2021

#include <iostream>

using namespace std;

class EncryptableString
{
private:
	string str;

public:
	EncryptableString(string str)
	{
		this->str = str;
	}

	void encrypt()
	{
		string encrypted_str = "";

		for (int i = 0; i < str.length(); i++)
			if (str[i] == 'z')
				encrypted_str += 'a';
			else if (str[i] == 'Z')
				encrypted_str += 'A';
			else
				encrypted_str += (str[i] + 1);

		cout << "Your encrypted string is: " << encrypted_str << endl;
	}
};

int main()
{
	string str;

	cout << "Enter a sentence to be encrypted: ";
	cin >> str;

	EncryptableString message(str);

	message.encrypt();
}