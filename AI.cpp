//Include required libraries
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
//Declare funtions
int createUser(string name);
int addUser(string name);
bool fexists(const char *filename);
//Main function
  int main() {
  //int isFile; unused variable
  //Make string name
  string name;
  string userfile;
  string pass;
  //Get name from user
  cout << "Hello, Welcome to Aqua-AI, Enter name now: ";
  getline(cin, name);
  cout << "Enter password for " << name << ":" << endl;
  getline(cin, pass);
  //If the file exists then add a user, else make a new file with the user
  userfile=name;
   if (fexists(userfile.append(".dat").c_str())){
      cout << "Welcome back, " << name << "." << endl;
    }
    else {
      createUser(name);
   }
  }
//Funtion createUser
  int createUser(string name){
  cout << "Creating user..." << endl;
  //Declare what file is
  string namefile;
  ofstream userfile;
  //Make a file
  cout << "Creating user files..." << endl;
  namefile=name;
  userfile.open(namefile.append(".dat").c_str());
    
  //Close the file
  userfile.close();
  cout << "User " << name << " has been created." << endl; 
  //End
  return 0;
  }
  

//Check if file exists
bool fexists(const char *filename) {
  ifstream ifile(filename);
  return ifile;
}
