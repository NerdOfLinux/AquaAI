#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main()
{
  string search;
  cout << "Would you like to search that on your browser?" << endl;
  getline(cin, search);
  replace(string.begin(), string.end(), ' ', '%20');
  if ( search == "yes" ) {
    system("echo What would you like to search ; read search ; x-www-browser https://www.google.com/#q=$search");
  } else {
    cout << "goodbye" << endl;
  }



return 0;
}
