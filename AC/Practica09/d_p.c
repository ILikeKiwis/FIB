#include <stdio.h>

int main() {
    double x, y, a;
    x = 665857;
    y = 470832;
    a = 4;
    double z;
    z = x*x*x*x - a*(y*y*y*y) - a * y *y;
    printf("Res: %f\n", z);
}