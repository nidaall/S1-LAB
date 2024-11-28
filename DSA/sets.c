#include <stdio.h>

int isPresent(int arr[], int size, int value);
void readSet(int set[], int universal[], int size);
void printSet(int set[], int size);


int n, n1, n2;


void main() 
{
	printf("Enter the size of the universal set: ");
	scanf("%d", &n);
	int U[n];
	printf("Enter the elements in the Universal Set: \n");
	readSet(U, NULL, n);

	printf("Enter the size of set 1: ");
	scanf("%d", &n1);
	if (n1 > n || n1 < 0) {
		printf("Invalid size!\n");
		return;
	}
	int set1[n1];
	printf("Enter the elements in set 1: \n");
	readSet(set1, U, n1);
	printf("Enter the size of set 2: ");
	scanf("%d", &n2);
	if (n2 > n || n2 < 0) {
		printf("Invalid size!\n");
		return;
	}
	int set2[n2];
	printf("Enter the elements in set 2: \n");
	readSet(set2, U, n2);

	int S1[n], S2[n];
	for (int i = 0; i < n; i++) {
		S1[i] = 0, S2[i] = 0;
		for (int j = 0; j < n1; j++) {
			if (U[i] == set1[j]) {
				S1[i] = 1;
				break;
			}
		}
		for (int j = 0; j < n2; j++) {
			if (U[i] == set2[j]) {
				S2[i] = 1;
				break;
			}
		}
	}

	int setUnion[n];
	for (int i = 0; i < n; i++) {
		if (S1[i] == 1 || S2[i] == 1)
			setUnion[i] = 1;
		else
			setUnion[i] = 0;
	}

	int setIntersection[n];
	for (int i = 0; i < n; i++) {
		if (S1[i] == 1 && S2[i] == 1)
			setIntersection[i] = 1;
		else
			setIntersection[i] = 0;
	}

	printf("U    : ");
	printSet(U, n);
	printf("Set 1: ");
	printSet(S1, n);
	printf("Set 2: ");
	printSet(S2, n);
	printf("S1uS2: ");
	printSet(setUnion, n);
	printf("S1nS2: ");
	printSet(setIntersection, n);
}


int isPresent(int arr[], int size, int value) {
	for (int i = 0; i < size; i++) {
		if (arr[i] == value)
			return 1;
	}
	return 0;
}

void readSet(int set[], int universal[], int size) {
	int element;
	for (int i = 0; i < size; i++) {
		printf("Element %d: ", i + 1);
		scanf("%d", &element);
		if (!isPresent(set, i, element) && (universal == NULL || isPresent(universal, n, element))) {
			set[i] = element;
		} else {
			printf("Invalid Entry!\n");
			i--;
		}
	}
}

void printSet(int set[], int size) {	
	for (int i = 0; i < size; i++) {
		printf("%d ", set[i]);
	}
	printf("\n");
}