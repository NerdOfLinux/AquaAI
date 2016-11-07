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
int learn(string newInfo);
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

//Function to open browser with a custom search term
int search(string searchTerm) {
  string searchyesno;
  string bash;
  cout << "Would you like to search that on your browser?" << endl;
  getline(cin, searchyesno);
  //If user responds yes then
  if ( searchyesno == "yes" ) {
    bash="search2=$(echo ";
    bash+=searchTerm;
    bash+=" | sed 's/ /%20/g'); x-www-browser https://www.google.com/#q=$search2";
    //Run a bash command to open a new browser window or tab with a search term
    system(bash.c_str());
  } else {
    cout << "goodbye" << endl;
    return 0;
  }
return 0;
}

int learn(string newInfo) {
  cout << "Test" << endl;
}
