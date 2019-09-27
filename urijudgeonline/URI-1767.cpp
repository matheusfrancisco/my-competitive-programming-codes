#include <stdio.h>
#include <stdlib.h>
 
/* Função boolean_bag recebe como parâmetro:
    1 - vetor v contendo os valores de importância dos objetos (ou a quantidade de brinquedos);
    2 - vetor w representando o peso de cada respectivo valor de importância do objeto
    3 - inteiro W representando o peso máximo da mochila;
    4 - inteiro n representando a quantidade de elementos que os vetores v e w contém.*/
int *boolean_bag(int *v, int *w, int W, int n);
 
int max(int a, int b);
 
/* Função que retorna o peso dos objetos maxizimizado pela função boolean_bag e os que sobraram */
void counterPesoSobra(int *w, int *resp, int n, int *pAndS);
 
int main(void){
 
    int *v, *w, result, *resp, pAndS[2], pac, i, N;
 
    scanf("%d", &N);
    while(N > 0)
        {
 
        pac = 0; /* n */
        scanf("%d", &pac);
 
        v = (int *) malloc((pac+1) * sizeof(int)); /* vetor de valores de importancia*/
        w = (int *) malloc((pac+1) * sizeof(int)); /* vetor de pesos*/
        resp = (int *) malloc((pac+1) * sizeof(int)); /* vetor de resposta*/
 
        v[0] = 0;
        w[0] = 0;
 
        for (i = 1; i <= pac; i++)
        {
            scanf("%d", &*(v+i));
            scanf("%d", &*(w+i));
        }
 
        resp = boolean_bag(v, w, 50, pac);
 
        result = resp[0];
        counterPesoSobra(w, resp, pac, pAndS);
 
        printf("%d brinquedos\n", result);
        printf("Peso: %d kg\n", pAndS[0]);
        printf("sobra(m) %d pacote(s)\n", pAndS[1]);
        printf("\n");
 
        free(v); /* Desalocando memória */
        free(w);
        free(resp);
    N--;
    }
    return 0;
}
 
int *boolean_bag(int *v, int *w, int W, int n)
{
    int t[n+1][W+1], Y, i, a, b, *vector = (int *) malloc( (n+1) * sizeof(int)) ;
 
    for (Y = 0; Y <= W; Y++)
    {
        t[0][Y]= 0;
        for (i = 1; i <= n; i++) { a = t[i-1][Y]; if (w[i] > Y)
                b = 0;
            else
                b = t[i-1][Y-w[i]] + v[i];
            t[i][Y] = max(a,b);
        }
    }
 
    /* Montando o vetor com os elementos selecionados*/
 
    for (a = 0; a < n; a++) vector[a] = 0; a = n; /* a recebe a qtd de linhas */ b = W; /* b recebe o peso máximo da bolsa, que também e o número de colunas*/ for (; a >= 1; a--)
    {
        if (t[a][b] == t[a-1][b]) /* Se o valor for igual ao anterior objeto não faz parte da solução ótima */
            vector[a] = 0;
        else
        {
            vector[a] = 1;
            b = b - w[a]; /* descontando o peso do objeto usado de b*/
        }
    }
 
    vector[0] = t[n][W]; /* Primeira posição do vetor alocado (malloc) contém a qtd maximizada dos brinquedos */
 
    return vector;
    /*return t[n][W];*/
}
 
int max(int a, int b)
{
    if (a >= b)
        return a;
    else
        return b;
}
 
void counterPesoSobra(int *w, int *resp, int n, int *pAndS)
{
    int i = 1, peso = 0, sobra = 0;
 
    for (; i <= n; i++)
    {
        if (resp[i] == 1)  /* Igual a 1 objeto selecionado */
            peso += w[i];
        else
            sobra += 1;
    }
    pAndS[0] = peso;
    pAndS[1] = sobra;
 
}
