
#ifndef LABORATOR2_REZOLV56_H
#define LABORATOR2_REZOLV56_H
//returneaza 1 daca nr dat e prim si 0 in mod contrar
int prim(int n);
//afiseaza secventa on functie de lungimea acesteia si pozitia finala
void afissecv(int x[],int pozf,int lmax);
//afla si transmite prim parametrii secventa de lungime maxima in care diferenta dintre numere este numar prim
void dif(int x[],int n,int &pozf,int &lmax);
//afla si trimite prin parametrii secventa de lungime maxima care se afla in intervalul inchis transmis prin parametrii
void interval(int x[],int n,int a,int b,int &pozf,int &lmax);
#endif //LABORATOR2_REZOLV56_H
