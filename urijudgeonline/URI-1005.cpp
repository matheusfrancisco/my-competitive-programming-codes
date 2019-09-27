#include <iostream>
 
using namespace std;
 
int main()
{
    double A,B,MEDIA;

    cin>>A;
    while(A>10.0|| A<0){
    cin>>A;
    };
    cin>>B;
    while(B>10.0 || B<0){
    cin>>B;
    };
    MEDIA = (A*3.5)+ (B*7.5);
    MEDIA = MEDIA/11;


    std::cout.precision(5);
    std::cout << std::fixed<<  "MEDIA = "<<MEDIA<<"\n" ;

    return 0;
}
