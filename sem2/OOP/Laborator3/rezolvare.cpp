//4 7
#include <iostream>
#include "rezolvare.h"
void afissecv(int x[],int pozi,int pozf)
{   std::cout<<"Secventa este:";
    for(int i=pozi;i<=pozf;i++)
        std::cout<<x[i]<<" ";
    std::cout<<" "<<std::endl;
}
int distincte(int x, int y, int v[])
{
    for(int i=x; i<=y-1; i++)
    {
        for(int j=i+1; j<=y; j++)
            if(v[i]==v[j])
                return 0;
    }
    return 1;
}
void distincte(int x[], int n, int &pozi, int &pozf)
{
    int l=0, lmax=0;
    for(int i=0; i<n-1; i++)
    {
        for(int j=i+1; j<n; j++)
        {
            if(distincte(i, j, x))
            {
                l=j-i+1;
                if(l>lmax)
                {
                    lmax=l;
                    pozi=i;
                    pozf=j;
                }
            }
        }
    }

}
void semnedif(int x[],int n,int &pozf,int &lmax)
{
    int s1=0,l=2,a,s2=0;
    if(x[0]-x[1]<0)
        s1=-1;
    else
        s1=1;
    a=x[1];
    for(int i=2;i<n;i++)
    {
        if(a-x[i]<0)
            s2=-1;
        else
            s2=1;
        a=x[i];
        if(s1!=s2)
        {
            l++;
            if(l>lmax)
            {
                lmax=l;
                pozf=i;
            }
        }
        else
            l=2;
        a=x[i];
        s1=s2;
    }
}
