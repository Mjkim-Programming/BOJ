#include <iostream>

using namespace std;

int main() {
    int year = 2024;
    int month = 1;
    int N;
    cin >> N;
    int total = (month - 1) + 7*N;
    year += total / 12;
    month = (total % 12) + 1;
    cout << year << " " << month;
    
    return 0;
}