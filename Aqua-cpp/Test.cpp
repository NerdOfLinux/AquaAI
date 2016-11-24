//Include required libraries
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <algorithm>
using namespace std;
//Declare funtions
int learn(string newInfo);
int read();
int check(string checkInfo);
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
