#include <iostream>
#include "citaf.h"
using namespace std;
void citire(int x[],int &n)
{   std::cout<<"Lungimea sirului este:";
    std::cin>>n;
    std::cout<<"Sirul citit este:";
    for(int i=0;i<n;i++)
        std::cin>>x[i];
}
void afisare(int x[],int n)
{
    std::cout<<"Sirul este: ";
    for(int i=0;i<n;i++)
        std::cout<<x[i]<<" ";
    std::cout<<endl;
}