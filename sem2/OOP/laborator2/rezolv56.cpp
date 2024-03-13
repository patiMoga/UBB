#include <iostream>
#include "rezolv56.h"
using namespace std;
int prim(int n)
{
    if(n<2)
        return 0;
    for(int d=2;d<=n/2;d++)
        if(n%d==0)
            return 0;
    return 1;
}
void afissecv(int x[],int pozf,int lmax)
{   std::cout<<"Secventa este:"<<std::endl;
    for(int i=pozf-lmax+1;i<=pozf;i++)
        std::cout<<x[i]<<" ";
    std::cout<<" "<<endl;
}
void dif(int x[],int n,int &pozf,int &lmax)
{
    int a,d,l=1;
    a=x[0];
    for(int i=1;i<n;i++)
    {
        if (x[i] > a)
            d = x[i] - a;
        else
            d = a - x[i];
        if(prim(d))
        {
            l++;
            if(l>lmax)
            {
                lmax=l;
                pozf=i;
            }
        }
        else
            l=1;
        a=x[i];

    }
}
void interval(int x[],int n,int a,int b,int &pozf,int &lmax)
{
    int l=0;
    for(int i=0;i<n;i++)
    {
        if(x[i]>=a&&x[i]<=b)
        {
            l++;
            if(l>lmax)
            {
                lmax=l;
                pozf=i;
            }
        }
        else
            l=0;
    }
}