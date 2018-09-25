#include <iostream>
#include <string>

using namespace std;

string keyRaces(int s, int v1, int v2, int t1, int t2) {
    int player1 = 2*t1 + v1*s;
    int player2 = 2*t2 + v2*s;
    return (player1 < player2)? "First":(player1 > player2)? "Second":"Friendship";
}
int main() {
    int s, v1, v2, t1, t2;
    cin >> s;
    cin >> v1;
    cin >> v2;
    cin >> t1;
    cin >> t2;
    cout << keyRaces(s, v1, v2, t1, t2) << endl;
    return 0;
}