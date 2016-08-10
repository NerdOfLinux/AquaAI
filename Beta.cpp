#include <iostream>
using namespace std;

int main()
{
	//Define username as a string
	string username;
	//Print Welcome to AquaAI
	cout << "Welcome to AquaAI." << endl;
	//Get username
	cout << "Please enter your username: ";
	getline (cin, username);
	//Print Welcome
	cout << "Welcome, " << username << "." << endl;
	
	//exit
	return 0;
}
