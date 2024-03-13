
#ifndef LABORATOR4_REPOSITORY_H
#define LABORATOR4_REPOSITORY_H
#include "patrat.h"
#include <vector>
class Repo
{
private:
    std::vector <Patrat> lista;

public:
    Repo();
    ~Repo();
    void add(Patrat &p);
    Patrat getbyPos(int pos);
    int getSize();
};

#endif //LABORATOR4_REPOSITORY_H
