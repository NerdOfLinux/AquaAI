#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main()
{
  string search;
  cout << "Would you like to search that on your browser?" << endl;
  getline(cin, search);
  if ( search == "yes" ) {
    system("echo What would you like to search ; read search ; search2=${search// /%20}; x-www-browser https://www.google.com/#q=$search2");
  } else {
    cout << "goodbye" << endl;
  }



return 0;
}
