#include <stdio.h>

int main()
{
    double raio,pi,A;
    pi =3.14159;
    scanf("%lf",&raio);
    A = pi * (raio * raio);

    printf("A=%.4lf\n",A);
    return 0;
}

