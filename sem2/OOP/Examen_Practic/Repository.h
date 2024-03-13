//
// Created by ARDELE on 5/30/2022.
//

#ifndef EXAMEN_PRACTIC_30_05_2022_REPOSITORY_H
#define EXAMEN_PRACTIC_30_05_2022_REPOSITORY_H
#include "Bacterie.h"
#include "vector"


class Repository {
private:
    std::vector<Bacterie> entitati;
public:
    Repository();
    Repository(const Repository &rep);
    void addElem(const Bacterie &b);
    int getnoelem();
    int getsize();
    Bacterie getElem(int poz);
    std::vector<Bacterie>::iterator getAll();
    ~Repository();
};


#endif //EXAMEN_PRACTIC_30_05_2022_REPOSITORY_H
