//Include required libraries
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int createUser(string name);
  int main() {
  string name;
  cout << "Hello, Welcome to Aqua-AI, Enter name now: ";
  getline(cin, name);
  output=createUser(name);
  cout << output << endl;
}

  int createUser(string name){
  ofstream file;
  file.open("AI.dat");
  file << name;
  file << "\n";
  file.close();
  cout << "Welcome, " << name << "." << endl;
  return 0;
  }
