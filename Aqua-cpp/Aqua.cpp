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
int read(string oldInfo);
//Make a string called searchTerm, newInfo, name, command, and userfile
string searchTerm;
string newInfo;
string name;
string command;
string userfile;
//Main function
  int main() {
  //Get name from user
  cout << "Hello, Welcome to Aqua-AI, Enter name now: ";
  getline(cin, name);
  //Make name2 to edit, keep name as original input
	string name2=name;
  //If the file exists then add a user, else make a new file with the user
   userfile=name2.append(".dat");
   if (fexists(userfile.c_str())){
   	cout << "Welcome, " << name << ". Use exit to exit." << endl;
   	//While the input is not equal to exit
	while ( command != "exit" ) {
		//Print Enter new info
      		cout << "Enter info/question: ";
      		//Get user input
      		getline(cin, command);
      		newInfo=command; 
      		//Run function learn with string newInfo
		learn(newInfo); }
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
  main();
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
  //Make string called yesno and bash
  string searchyesno;
  string bash;
  cout << "Would you like to search that on your browser?: ";
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

//Make function learn with string newInfo
int learn(string newInfo) {
  ofstream file;
  //Open the userfile to append
  file.open(userfile.c_str(), ios_base::app);
  //Write to the file if newInfo is not equal to exit
  if (newInfo != "exit") { 
  file << newInfo << endl; }
}

int read(string oldInfo) {
	string line;
	ifstream readfile(userfile.c_str());
	while (getline(readfile, line)){
		cout << line << '\n';	
	}
}
