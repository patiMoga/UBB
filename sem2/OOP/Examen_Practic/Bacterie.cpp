//
// Created by ARDELE on 5/30/2022.
//

#include "Bacterie.h"

Bacterie::Bacterie() {
    ///constructor fara paramentrii
    denumire="";
    varsta=0;
    tip="";
}

Bacterie::Bacterie(std::string denumire, int varsta, std::string tip) {
///constructorul cu parametrii
    /// \param denumire: numele bacteriei
    /// \param vasrta: varsata bacteriei
    /// \param tip: tipul bacteriei
    this->denumire=std::move(denumire);
    this->varsta=varsta;
    this->tip=std::move(tip);

}

Bacterie::Bacterie(const Bacterie &b) {
///constructorul cu parametrii
    /// \param denumire: numele bacteriei
    /// \param vasrta: varsata bacteriei
    /// \param tip: tipul bacteriei
    this->denumire=b.denumire;
    this->varsta=b.varsta;
    this->tip=b.tip;
}

Bacterie::~Bacterie() {
///destructor

}

Bacterie Bacterie::operator=(const Bacterie &b) {
    ///operatorul de atribuire
    if (this != &b)
    {
        this->denumire=b.denumire;
        this->varsta=b.varsta;
        this->tip=b.tip;

        return *this;

    }
}

std::string Bacterie::getnume() {
    ///getter pentru nume
    return denumire;
}

int Bacterie::getvarsta() {
    ///getter pentru varsta
    return varsta;
}

std::string Bacterie::gettip() {
    ///getter pentru tip
    return tip;
}

void Bacterie::setdenumire(std::string denumire) {
    ///setter pentru nume
    this->denumire= move(denumire);
}

void Bacterie::setxa(int varsta) {
///setter pentru varsta
    this->varsta=varsta;
}

void Bacterie::settip(std::string tip) {
///setter pentru nume
    this->tip= move(tip);

}
