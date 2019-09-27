#include <iostream>
 
using namespace std;


int main()
{
    int c1,c2,nc1,nc2;
    double vc1,vc2,valortotal;

    cin>>c1>>nc1 >>vc1 ;
    while(nc1<0.0){
    cin>>nc1;
    };
    while(vc1<0.0){
    cin>>vc1;
    };
        cin>>c2>>nc2 >>vc2 ;
    while(nc2<0.0){
    cin>>nc2;
    };
    while(vc2<0.0){
    cin>>vc2;
    };
    valortotal = (nc2*vc2) + (nc1*vc1);
     std::cout.precision(2);
    std::cout << std::fixed<<  "VALOR A PAGAR: R$ "<<valortotal<<"\n" ;
    return 0;



}
