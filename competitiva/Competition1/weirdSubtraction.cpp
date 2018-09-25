#include <iostream>
#include <string>

using namespace std;

void subtract(long long a, long long b) {
    while (a && b) {
        if (a >= 2*b) {
            a %= (2*b);
        }else if (b >= 2*a) {
            b %= (2*a);
        }else{
            break;
        }
    }
    cout << a << " " << b << endl;
}
int main() {
    long long a, b;
    cin >> a;
    cin >> b;
    subtract(a, b);
    return 0;
}