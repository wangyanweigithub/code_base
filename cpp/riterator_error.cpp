#include <vector>
#include <array>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;


int main() 
{
	array<int, 5> col1 = { 1, 2, 3, 4, 5, 6, 7 };
	cout << *(col1 + 2) << endl; 

	vector<int>::const_iterator pos;
	pos = find(col1.cbegin(), col1.cend(), 5);
	
	cout << "pos: " << *pos << endl;

	vector<int>::const_reverse_iterator rpos(pos);
	//cout << "rpos: " << *rpos  << "pos" << pos - col1<< endl;

}
