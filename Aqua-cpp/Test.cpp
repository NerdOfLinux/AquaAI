//Include required libraries
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <algorithm>
using namespace std;
//Declare funtions
int createUser(string name);
int addUser(string name);
bool fexists(const char *filename);
int search(string searchTerm);
int learn(string newInfo);
int read(string oldInfo);
int check(string checkInfo);
//Declare strings for use in code
string searchTerm;
string newInfo;
string name;
string command;
string userfile;
string search1;
string que;

int length=10; //Declare length and set it to ten
//Main function
  int main() {
	read();
  }

//Make function learn with string newInfo
int learn(string newInfo) {
  ofstream file;
  //Open the userfile to append
  file.open(userfile.c_str(), ios_base::app);
  //Write to the file if newInfo is not equal to exit
  if (newInfo != "exit") { 
  file << newInfo << endl; }
}

int read() {
	string line;
	ifstream readfile(userfile.c_str());
	while (getline(readfile, line)){
		cout << line << '\n';	
	}
int check(string checkInfo) {
	cout << "Test." << endl;	
}
}
