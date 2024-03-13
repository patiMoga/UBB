
#include "Produse.h"
#include <iostream>

Produse::Produse(int cod, string name, int pret): cod(cod), nume(name), pret(pret){}


bool Produse::operator==(const Produse &produs) {
    return(this->cod == produs.cod && this->nume == produs.get_name() && this->pret == produs.pret);
}