#include <iostream>
using namespace std;
int main(void)
{
 int A;
 int fat[9];
 fat[0] = 1;
 fat[1] = 1;
 fat[2] = 2;
 fat[3] = 6;
 fat[4] = 24;
 fat[5] = 120;
 fat[6] = 720;
 fat[7] = 5040;
 fat[8] = 40320;
 fat[9] = 362880;
 
 cin>> A;
 
 int x =0;
 for(int i=9; i>=0 ; i--)
 {
  x +=(A/fat[i]);
  A = A%fat[i];
 }

 cout<<x<<endl;
}
