#include "repository.h"

Repo::Repo()
{
}
Repo::~Repo(){}
void Repo::add(Patrat &p)
{
    lista.push_back(p);
}
Patrat Repo::getbyPos(int pos)
{
    return lista.at(pos);
}
int Repo::getSize()
{
    return lista.size();
}
