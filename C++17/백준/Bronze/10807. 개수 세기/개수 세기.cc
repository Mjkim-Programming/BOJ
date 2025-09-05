#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    int arr[T];
    int count = 0;
    int flag;
    for(int i = 0; i < T; i++) {
        cin >> arr[i];
    }
    cin >> flag;
    for(int j = 0; j < T; j++) {
        if(arr[j] == flag) {
            count++;
        }
    }
    cout << count;
    
    return 0;
}