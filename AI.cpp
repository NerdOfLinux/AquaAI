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

  //Get name from user
  cout << "Hello, Welcome to Aqua-AI, Enter name now: ";
  getline(cin, name);
  //If the file exists then add a user, else make a new file with the user
   if (fexists("users.dat")){
      addUser(name);
    }
    else {
      createUser(name);
   }
  }
//Funtion createUser
  int createUser(string name){
  //Declare what file is
  string namefile;
  ofstream file;
  ofstream userfile;
  //Make a file
  file.open("users.dat");
  namefile=name;
  userfile.open(namefile.append(".dat").c_str());
  //Make a file
  file.open("users.dat");
  //Put the name in the file
  file << name;
  //Add a newline
  file << "\n";
  //Close the file
  file.close();
  userfile.close();
  cout << "Welcome, " << name << "." << endl;
  //End
  return 0;
  }
  
//Funtion addUser
  int addUser(string name){
  //Declare what file is
  ofstream file;
  ofstream userfile;
  string namefile;
  //Make a file
  namefile=name;
  file.open("users.dat", ios_base::app);
  userfile.open(namefile.append(".dat").c_str());
  file.open("users.dat", ios_base::app);
  //Put the name in the file
  file << name;
  //Add a newline
  file << "\n";
  //Close the file
  file.close();
  userfile.close();
  cout << "Welcome, " << name << "." << endl;
  return 0;
  }

//Check if file exists
bool fexists(const char *filename) {
  ifstream ifile(filename);
  return ifile;
}
