//Include required libraries
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;
//Declare funtions
int createUser(string name);
int addUser(string name);
bool fexists(const char *filename);
int search(string searchTerm);
string searchTerm;
//Main function
  int main() {
  //int isFile; unused variable
  //Make string name
  string name;
  string userfile;
  //Get name from user
  cout << "Hello, Welcome to Aqua-AI, Enter name now: ";
  getline(cin, name);
  //If the file exists then add a user, else make a new file with the user
  userfile=name;
   if (fexists(userfile.append(".dat").c_str())){
      cout << "Welcome, " << name << "." << endl;
      cout << "Enter item to search: ";
      getline(cin, searchTerm);
      search(searchTerm);
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
  //Define namefile
  namefile=name;
  userfile.open(namefile.append(".dat").c_str());
  //Close the file
  userfile.close();
  cout << "User " << name << " has been created." << endl; 
  cout << "Run this program again to log in." << endl;
  //End
  return 0;
  }
//Check if file exists
bool fexists(const char *filename) {
  ifstream ifile(filename);
  return ifile;
}

int search(string searchTerm) {
  string searchyesno;
  cout << "Would you like to search that on your browser?" << endl;
  getline(cin, searchyesno);
  if ( searchyesno == "yes" ) {
    //system("search2=$(echo $searchTerm | sed 's/ /%20/g'); x-www-browser https://www.google.com/#q=$search2");
    system("echo $searchTerm");
    cout << searchTerm << endl;
  } else {
    cout << "goodbye" << endl;
    return 0;
  }



return 0;
}
