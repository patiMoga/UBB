//
// Created by ARDELE on 5/30/2022.
//

#include "Repository.h"

Repository::Repository() {
///constructorul fara parametrii
}

Repository::Repository(const Repository &rep) {
    ///constructorul de copiere
    for (int i=0; i<rep.entitati.size(); i++)
    {
        this->entitati[i] = rep.entitati[i];
    }
}

void Repository::addElem(const Bacterie &b) {
    ///metoda add pentru entitatea problemei
    /// \param &t: entitatea transmisa prin referinta din service
    this->entitati.push_back(b);
}

int Repository::getnoelem() {
    ///returnarea numarului de elemente ale repository ului
    return int(this->entitati.size());
//    sort(triunghiuri.begin(),triunghiuri.end(),)
}

int Repository::getsize() {
    ///returnarea lungimii repository ului

    return int(this->entitati.size());
}

Bacterie Repository::getElem(int poz) {
    ///returnarea unui element din repository dupa pozitie
    /// \param poz: pozitia dde pe care se returneaza elementul
    return this->entitati[poz];
}

std::vector<Bacterie>::iterator Repository::getAll() {
    /// functie de returnare a tuturor entitatilor din repository
    return this->entitati.begin();
}


Repository::~Repository() =default;
///destructor pentru repository
