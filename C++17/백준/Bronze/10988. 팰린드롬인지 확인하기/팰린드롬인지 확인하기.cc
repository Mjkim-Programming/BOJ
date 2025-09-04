#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool is_palindrome(string str) {
    bool flag = true;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] != str[str.size()-1-i]) {
            flag = false;
            break;
        }
    }

    return flag;
}

int main() {
    string s;
    cin >> s;
    if (is_palindrome(s)) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }
    return 0;
}