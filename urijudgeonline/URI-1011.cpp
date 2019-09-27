#include <iostream>
 
using namespace std;

int main()
{
    double raio,volume,pi;
    pi = 3.14159;
    cin>>raio;
    while(raio < 0.0){
    cin>>raio;
    }
    volume = (4.0/3)*(pi)*(raio*raio*raio);
         std::cout.precision(3);
    std::cout << std::fixed<<  "VOLUME = "<<volume<<endl ;
    return 0;
}
