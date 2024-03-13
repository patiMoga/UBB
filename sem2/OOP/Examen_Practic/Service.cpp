//
// Created by ARDELE on 5/30/2022.
//
#include "iostream"
#include "Service.h"
#include "Bacterie.h"
#include "string"
#include "vector"

void Service::AddElement(std::string denumire, int varsta, std::string tip)
{
    /// functia de add din service
    /// \param denumire: numele bacteriei
    /// \param vasrta: varsata bacteriei
    /// \param tip: tipul bacteriei
    Bacterie b(denumire, varsta, tip);
    auto rez = this->repo.getAll();
    int c=0;
    for (int i=0;i < this->repo.getsize(); ++i)
    {
        if (rez[i].getnume()==denumire)
            c=1;
    }
    if (c==0) this->repo.addElem(b);
    else
        std::cout<<"Numele exista deja."<<std::endl;
}
void Service::showall()
{
    ///functia de afisare a tuturor entitatilor din repository
    auto rez = this->repo.getAll();

    for (int i=0;i < this->repo.getsize(); ++i)
    {
        std::cout << i + 1 << ". " << rez[i].getnume() << " - " << rez[i].getvarsta()<<" - "<< rez[i].gettip()<< std::endl;
    }
}


Service::Service(const Repository &repo) {
    ///constructorul cu parametrii ai service ului
    this->repo=repo;

}

void Service::afisaredupatipulbacteriei(std::string tip) {
    auto rez = this->repo.getAll();
    int c=0;
    std::vector<Bacterie> bacterii;
    //vector<Dreapta> dreptecompatibile;
    for (int i=0;i < this->repo.getsize(); ++i)
    {
        if (tip==rez[i].gettip())
        {
            bacterii.push_back(rez[i]);
            std::cout << i + 1 << ". " << rez[i].getnume() << " - " << rez[i].getvarsta()<<" - "<< rez[i].gettip()<< std::endl;

        }
    }
}
void Service::afisaredupatimp(int timp) {
    auto rez = this->repo.getAll();
    std::vector<Bacterie> bacterii;
    for (int i=0;i < this->repo.getsize(); ++i)
    {
        //std::cout<<"neimplementat"<<std::endl;
        if ( (rez[i].gettip()=="tip2") && (timp==3) ) {
//            std::cout << rez[i].gettip() << std::endl;
            bacterii.push_back(rez[i]);
            Bacterie b2(rez[i].getnume(), rez[i].getvarsta(), "tip1");
            bacterii.push_back(b2);
        }
        else
            bacterii.push_back(rez[i]);

    }

    for (int i=0;i < bacterii.size(); ++i)
    {
        std::cout << i + 1 << ". " << bacterii[i].getnume() << " - " << bacterii[i].getvarsta()<<" - "<< bacterii[i].gettip()<< std::endl;
    }
}

int Service::mediadevarsta() {
    auto rez = this->repo.getAll();
    int varsta_med = 0 ;
    int varsta_minima= INT_MAX;
    int varsta_maxima= 0;
    std::vector<Bacterie> bacterii;
    //vector<Dreapta> dreptecompatibile;
    for (int i=0;i < this->repo.getsize(); ++i) {
        if (varsta_minima > rez[i].getvarsta()) varsta_minima= rez[i].getvarsta();
        if (varsta_maxima < rez[i].getvarsta()) varsta_maxima= rez[i].getvarsta();

    }
    if (varsta_minima != 0) varsta_med= (varsta_minima + varsta_maxima)/2;

    return varsta_med;
}
