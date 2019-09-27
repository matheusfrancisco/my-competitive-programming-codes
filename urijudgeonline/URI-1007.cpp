#include <iostream>
 
using namespace std;
 
int main()
{
    int A,B,C,D,DIFERENCA;

    cin>>A;

    cin>>B;

    cin>>C;
    cin>>D;

    DIFERENCA = (A*B) - (C*D) ;

    std::cout << std::fixed<<  "DIFERENCA = "<<DIFERENCA<<"\n" ;

    return 0;
}
