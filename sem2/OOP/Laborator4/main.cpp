#include <iostream>
#include "tests.h"
#include "patrat.h"
#include "repository.h"
#include "operations.h"
int main()
    {Repo repo;
    test_domain();
    testopp();
    testrepo();
    int opt;
    while(true)
    {
        std::cout<<"1.Adaugare."<<std::endl<<"2.Afisare."<<std::endl<<"3.Cea mai mare entitate."<<std::endl<<"4.Apartine cadranului 1."<<std::endl<<"5.Secventa de patrate cu latura egala."<<std::endl<<"0.Exit."<<std::endl;
        std::cout<<"Optiunea aleasa este:";
        std::cin>>opt;
        switch(opt)
        {
            case 1:
            {   int a,x,y;
                std::cout<<"Latura patratului este: ";
                std::cin>>a;
                std::cout<<"Coordonatele sunt:";
                std::cin>>x;
                std::cin>>y;
                Patrat p(a,x,y);
                repo.add(p);
                break;
            }
            case 2:
            {   int n=repo.getSize();
                for(int i=0;i<n;i++)
                {
                    std::cout<<"Patratul "<<i+1<<" cu latura: "<<repo.getbyPos(i).get_lat()<<" "<<"si coordonatele:"<<repo.getbyPos(i).get_x()<<","<<repo.getbyPos(i).get_y()<<std::endl;
                }
                std::cout<<" "<<std::endl;
                break;
            }
            case 0:
                exit(1);
            case 3:
            {
                std::cout<<"Cel mai mare patrat este cel cu latura:"<<cmm(repo);
                std::cout<<std::endl;
                break;
            }
            case 4:
            {
                int n=repo.getSize();
                for(int i=0;i<n;i++)
                {
                    if(apcandran1(repo,i)==1)
                        std::cout<<"Patratul "<<i+1<<" cu latura "<<repo.getbyPos(i).get_lat()<<" se afla in cadranul 1"<<std::endl;
                }
                break;
            }
            case 5:
            {
                int lmax=1,pozf=0;
                Patrat p1;
                secventa(repo,pozf,lmax);
                int pozi=pozf-lmax+1;
                for(int i=pozi;i<=pozf;i++)
                    std::cout<<"Patratul"<<" "<<i+1<<" "<<repo.getbyPos(i).get_lat()<<std::endl;
                std::cout<<" "<<std::endl;
                break;
            }
        }
    }

    return 0;
}
