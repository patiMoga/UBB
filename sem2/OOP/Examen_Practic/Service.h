//
// Created by ARDELE on 5/30/2022.
//

#ifndef EXAMEN_PRACTIC_30_05_2022_SERVICE_H
#define EXAMEN_PRACTIC_30_05_2022_SERVICE_H
#include "iostream"
#include "Repository.h"
#include "string"

class Service {
private:
    Repository repo;
public:
    Service()=default;
    explicit Service(const Repository &repo);
    int getnoelements(){
        return this->repo.getnoelem();
    }
    void AddElement(std::string denumire, int varsta, std::string tip);
    void showall();
    void afisaredupatipulbacteriei(std::string tip);
    void afisaredupatimp(int timp);
    int mediadevarsta();
};


#endif //EXAMEN_PRACTIC_30_05_2022_SERVICE_H
