#include <stdio.h>
#define X 665857
#define Y 470832

int main() {
    double dX = X;
    double dY = Y;
    double dR = dX*dX*dX*dX - 4 * dY*dY*dY*dY - 4 * dY*dY;

    float fX = X;
    float fY = Y;
    float fR = fX*fX*fX*fX - 4 * fY*fY*fY*fY - 4 * fY*fY;

    long long lX = X;
    long long lY = Y;
    long long lR = lX*lX*lX*lX - 4 * lY*lY*lY*lY - 4 * lY*lY;

    printf("Simple precisión: %f \n", fR);
    printf("Doble precisión: %f \n", dR);
    printf("Long long: %lld \n", lR);
}   