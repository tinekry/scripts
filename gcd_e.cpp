#include <bits/stdc++.h>
int gcd_extended(int a, int b, int& x, int& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int d = gcd_extended(b, a%b, x1, y1);
    x = y1;
    y = x1 - a / b * y1;
    return d;
}

int main() {
    /*
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    */
    int a, b, c, x = 0, y = 0, d;
    std::cin >> a >> b >> c;
    d = gcd_extended(a, b, x, y);
    if (c % d == 0) {
        std::cout << "gcd = " << d << "\nans: " << c / d * x << " " << c / d * y;
    } else {
        std::cout << "Impossible";
    }
    return 0;
}


