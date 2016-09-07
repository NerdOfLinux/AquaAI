//Include required libraries
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
  int main() {
  createUser()
}

  int createUser(){
  string name;
  ofstream file;
  cout << "Hello, Welcome to Aqua-AI, Enter name now: ";
  getline(cin, name);
  cout << "Welcome, " << name << "." << endl;
  file.open("AI.dat");
  file << name;
  file << "\n";
  file.close();
  return 0;
  }
