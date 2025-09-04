#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    stack<int> s;
    for (int i = 0; i < N; i++) {
        int cmd;
        cin >> cmd;

        if (cmd == 1) {
            int x;
            cin >> x;
            s.push(x);
        }
        else if (cmd == 2) {
            if (!s.empty()) {
                cout << s.top() << "\n";
                s.pop();
            } else {
                cout << -1 << "\n";
            }
        }
        else if (cmd == 3) {
            cout << s.size() << "\n";
        }
        else if (cmd == 4) {
            cout << (s.empty() ? 1 : 0) << "\n";
        }
        else if (cmd == 5) {
            if (!s.empty()) {
                cout << s.top() << "\n";
            } else {
                cout << -1 << "\n";
            }
        }
    }
    return 0;
}