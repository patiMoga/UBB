#include <iostream>
#include "probl.h"
using namespace std;
void citire(int x[],int n)
{
    for(int i=0;i<n;i++)
        cin>>x[i];
}
void afisare(int x[],int n)
{
    for(int i=0;i<n;i++)
        cout<<x[i]<<" ";
    cout<<endl;
}

