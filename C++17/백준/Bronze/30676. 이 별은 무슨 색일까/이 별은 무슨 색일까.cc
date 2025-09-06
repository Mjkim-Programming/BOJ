#include <iostream>

using namespace std;

int main() {
    int gamma;
    cin >> gamma;
    if(gamma>=620) {
        cout << "Red";
    } else if(gamma>=590) {
        cout << "Orange";
    } else if(gamma>=570) {
        cout << "Yellow";
    } else if(gamma>=495) {
        cout << "Green";
    } else if(gamma>=450) {
        cout << "Blue";
    } else if(gamma>=425) {
        cout << "Indigo";
    } else {
        cout << "Violet";
    }
    
    return 0;
}