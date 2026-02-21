#include <stdio.h>

int main() {
    long long  x, y, a;
    x = 665857;
    y = 470832;
    a = 4;
    long long z;
    z = x*x*x*x - a*(y*y*y*y) - a * y *y;
    printf("Res: %lld\n", z);
}