#include <iostream>
 
using namespace std;
 

int main()
{
    double A,B,C,MEDIA;

    cin>>A;
    while(A>10.0|| A<0){
    cin>>A;
    };
    cin>>B;
    while(B>10.0 || B<0){
    cin>>B;
    };
    cin>>C;
    while(C>10.0 || C<0){
    cin>>C;
    };
    MEDIA = (A*2)+ (B*3) + (C*5);
    MEDIA = MEDIA/10;


    std::cout.precision(1);
    std::cout << std::fixed<<  "MEDIA = "<<MEDIA<<"\n" ;

    return 0;
}
