#include<iostream>
#include<vector>
#include<stack>
using namespace std;

#define MAX 100001
vector<vector<int>> children(MAX);

int parentList[MAX];

int N;

void Input() {
	cin >> N;
	for (int i = 1; i < N; i++) {
		int a, b;
		cin >> a >> b;
		children[a].push_back(b);
		children[b].push_back(a);
	}
}

void DFS() {
	stack<pair<int, int>> stk;
	stk.push(make_pair(-1, 1));

	while (!stk.empty()) {
		int parent = stk.top().first;
		int child = stk.top().second;
		stk.pop();

		parentList[child] = parent;

		for (auto node : children[child]) {

			if (node != parent) {
				stk.push(make_pair(child, node));
			}

		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	Input();
	DFS();
	
	for (int i = 2; i <= N; i++) {
		cout << parentList[i] << '\n';
	}
	return 0;
}