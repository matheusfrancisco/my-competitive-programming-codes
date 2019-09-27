#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <math.h>
#include <stdio.h>



using namespace std;


int main() {

    int n, i,v1,v2;
    double maiorQM, menorQM;
    int valores[1000];

    
    while(cin>>n && n) {
	

	    double total = 0.0;
	   
	    
	    for(i = 0; i < n; i++) 
	    {
	    	scanf("%d.%d", &v1, &v2);
	    	valores[i] = v1*100+v2;
	    	total += valores[i];
	    }

	    total = ((float)total)/n;
	   	maiorQM = 0.0;
	    menorQM = 0.0;
	    
	    
	    for(i = 0; i < n; i++) {
	    	if(valores[i] > total) 
	    	{
	    		maiorQM += ((int)(valores[i] - total))/100.0;
	    	}else
	    	{
	    		menorQM += ((int)(total - valores[i]))/100.0;
	    	}
	    	
	    }
	    if(menorQM > maiorQM)
	    {
	    printf("$%.2f\n", menorQM);
		}else{
		printf("$%.2f\n", maiorQM);
		}
    }
    return 0;
}
