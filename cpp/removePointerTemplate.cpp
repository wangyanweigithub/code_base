#include <iostream>

using namespace std;

//递归去除指针template
template<typename T>
class RemovePointer {
public:
	typedef T Result;
};

template<typename T>
class RemovePointer<T*> {
public:
	typedef typename RemovePointer<T>::Result Result;

};

int main() {
	RemovePointer<int**>::Result a = 23;

	cout << a << endl;
	return 0;
}
