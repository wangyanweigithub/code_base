#include <stdio.h>

int main() {
	char a = 'a';
	char* b = &a;
	printf("char is: %d, char* is: %d, *char is: %d", sizeof(a), sizeof(b), sizeof(*b));
	return 0;
}
