#include <iostream>
#include <vector>
using namespace std;

int main() {
	int C;
	cin >> C;
	for (int cases = 0; cases < C; cases++) {
		// Input
		int n, k, m;
		n = k = m = 0;
		int L[50] = { 0 };
		int Q[10] = { 0 };
		double T[50][50] = { 0.0 };
		cin >> n >> k >> m;
		for (int iter2 = 0; iter2 < n; iter2++) {
			cin >> L[iter2];
		}
		for (int iter2 = 0; iter2 < n; iter2++) {
			for (int iter3 = 0; iter3 < n; iter3++) {
				cin >> T[iter2][iter3];
			}
		}
		for (int iter2 = 0; iter2 < m; iter2++) {
			cin >> Q[iter2];
		}
		
		// Solve
		double startPosibilities[8][50] = { 0.0 };
		startPosibilities[0][0] = 1.0;
		int remainder;
		for (int minute = L[0]; minute < k + 1; minute++) {
			remainder = minute & 7;
			for (int song = 0; song < n; song++)
				startPosibilities[remainder][song] = 0.0;
			for (int from = 0; from < n; from++) {
				double a = startPosibilities[(remainder - L[from] + 8) & 7][from];
				for (int to = 0; to < n; to++) {
					double b = a * T[from][to];
					startPosibilities[remainder][to] = startPosibilities[remainder][to] + b;
				}
			}
		}

		// Output
		remainder = k & 7;
		for (int favorite = 0; favorite < m; favorite++) {
			double result = 0.0;
			for (int minute = 0; minute < L[Q[favorite]]; minute++) {
				result += startPosibilities[(8 + remainder - minute) & 7][Q[favorite]];
			}
			cout.precision(8);
			cout << fixed << result << " ";
		}
		cout << endl;
	}
}