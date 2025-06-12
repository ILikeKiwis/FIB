#include <stdio.h>

int main() {
    float x, y, a;
    x = 665857;
    y = 470832;
    a = 4;
    float z;
    z = x*x*x*x - a*(y*y*y*y) - a * y *y;
    printf("Res: %f\n", z);
}