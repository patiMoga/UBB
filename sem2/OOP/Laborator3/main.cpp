#include <iostream>
#include "citaf.h"
#include "rezolvare.h"
#include "tests.h"
//4 si 7
int main() {
    teste();
    int n,opt=-1,pozf,lmax,pozi;
    n=0;
    int *x=new int[100];
    while(opt!=0)
    {
        std::cout<<"0.Exit."<<std::endl<<"1.Citeste."<<std::endl<<"2.Afiseaza."<<std::endl;
        std::cout<<"3.Distincte"<<std::endl<<"4.Secventa de semne distincte la diferenta elementelor."<<std::endl;
        std::cout<<"Optiunea aleasa este:";
        std::cin>>opt;
        std::cout<<std::endl;
        if (opt==1)
        {
            citire(x,n);
        }
        else if(opt==2)
            afisare(x,n);
        else if(opt==0) {
            delete[] x;
            exit(0);
        }
        else if(opt==3)
        {
            pozf=0;
            lmax=1;
            distincte(x,n,pozi,pozf);
            std::cout<<"Secventa este:";
            for(int i=pozi;i<=pozf;i++)
                std::cout<<x[i]<<" ";
            std::cout<<" "<<std::endl;
        }
        else if(opt==4)
        {
            pozf=1;
            lmax=2;
            semnedif(x,n,pozf,lmax);
            pozi=pozf-lmax+1;
            std::cout<<"Secventa este:";
            for(int i=pozi;i<=pozf;i++)
                std::cout<<x[i]<<" ";
            std::cout<<" "<<std::endl;
        }

    }
    return 0;
}
