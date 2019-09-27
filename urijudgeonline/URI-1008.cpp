#include <iostream>
 
using namespace std;
 
int main()
{

    int number,horas;
    double salary,salarytotal;

    cin>>number;
    while(number<0.0){
    cin>>number;
    };
    cin>>horas;
    while(horas<0.0){
    cin>>horas;
    };
    cin>>salary;
    while(salary<0.0){
    cin>>salary;
    };
    salarytotal = (horas*salary);
    cout<<"NUMBER = "<<number<<endl;
    std::cout.precision(2);
    std::cout << std::fixed<<  "SALARY = U$ "<<salarytotal<<"\n" ;
    return 0;
}
