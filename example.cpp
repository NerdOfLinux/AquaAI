#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
string search;
cout << "Would you like to search that on google?" << endl;
getline(cin, search);

if ( search == "yes" ) {
system("echo What would you like to search ; read search ; x-www-browser $search");
} else {
cout << "goodbye" << endl;
}



return 0;
}
