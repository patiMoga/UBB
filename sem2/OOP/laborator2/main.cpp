#include <iostream>
#include "probl.h"
#include "rezolv56.h"
#include "tests.h"
using namespace std;

int main()
{
    teste();
    int x[100],n,a,b,opt=0,pozf,lmax;
    while(opt!=5)
    {
        std::cout<<"1.Citire."<<std::endl<<"2.Afisare."<<std::endl<<"3.Diferenta de prime."<<std::endl<<"4.Interval inchis."<<std::endl<<"5.Exit."<<std::endl;
        std::cout<<"Alege optiunea:";
        std::cin>>opt;
        if(opt==1){
            std::cout<<"Numarul de elemente adaugate:";
            std::cin>>n;
            std::cout<<"Elementele ce vor fi citite:";
            citire(x,n);}
        else
            if(opt==2)
                afisare(x,n);
            else
                if(opt==5)
                    exit(0);
                else
                    if(opt==3)
                    {   pozf=0;
                        lmax=0;
                        dif(x, n,pozf,lmax);
                        afissecv(x,pozf,lmax);
                    }
                    else
                        if(opt==4)
                        {
                            std::cout<<"Se da intervalul:";
                            std::cin>>a;
                            std::cin>>b;
                            pozf=0;
                            lmax=0;
                            interval(x,n,a,b,pozf,lmax);
                            afissecv(x,pozf,lmax);
                        }
    }


    return 0;
}
