//Include required libraries
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
//Declare funtions
int createUser(string name);
int addUser(string name);
<<<<<<< HEAD
bool fexists(const char *filename);
=======
bool userFile(const char *filename);
>>>>>>> d1d4d3f2822b6d6bba46bf5249117494c1f8abec
//Main function
  int main() {
  //int isFile; unused variable
  //Make string name
  string name;

  //Get name from user
  cout << "Hello, Welcome to Aqua-AI, Enter name now: ";
  getline(cin, name);
<<<<<<< HEAD
  //If the file exists then add a user, else make a new file
  if (fexists("users.dat") == false){
    createUser(name);
=======
  //If the file exists then add a user, else make a new file with the user
  if (userFile("users.dat")){
    addUser(name);
>>>>>>> d1d4d3f2822b6d6bba46bf5249117494c1f8abec
  }
  else {
    
  }
}
//Funtion createUser
  int createUser(string name){
  //Declare what file is
  string namefile;
  ofstream file;
<<<<<<< HEAD
  ofstream userfile;
  //Make a file
  file.open("users.dat");
  namefile=name;
  userfile.open(namefile.append(".dat").c_str());
=======
  ofstream fileAI;
  //Make a file
  fileAI.open("AI.dat");
  file.open("users.dat");
>>>>>>> d1d4d3f2822b6d6bba46bf5249117494c1f8abec
  //Put the name in the file
  file << name;
  //Add a newline
  file << "\n";
  //Close the file
  file.close();
<<<<<<< HEAD
  userfile.close();
=======
  fileAI.close();
>>>>>>> d1d4d3f2822b6d6bba46bf5249117494c1f8abec
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
<<<<<<< HEAD
  namefile=name;
  file.open("users.dat", ios_base::app);
  userfile.open(namefile.append(".dat").c_str());
=======
  file.open("users.dat", ios_base::app);
>>>>>>> d1d4d3f2822b6d6bba46bf5249117494c1f8abec
  //Put the name in the file
  file << name;
  //Add a newline
  file << "\n";
  //Close the file
  file.close();
<<<<<<< HEAD
  userfile.close();
=======

>>>>>>> d1d4d3f2822b6d6bba46bf5249117494c1f8abec
  cout << "Welcome, " << name << "." << endl;
  return 0;


  }
<<<<<<< HEAD

bool fexists(const char *filename) {
=======
//Check if file exists
bool userFile(const char *filename) {
>>>>>>> d1d4d3f2822b6d6bba46bf5249117494c1f8abec
  ifstream ifile(filename);
  return ifile;
}
