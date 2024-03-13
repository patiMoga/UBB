
#ifndef LAB_4_5_SD_V1_ATM_H
#define LAB_4_5_SD_V1_ATM_H

#include "Tranzactie.h"
#include "List.h"
#include "Colectie.h"
#include <vector>

class ATM {
private:
    Colectie colectie;
    vector<Tranzactie> tranzactii;
public:
    void printMenu();
    void afisareColectie();
    void plateste();
    void showTranzactii();
    void runATM();
};


#endif //LAB_4_5_SD_V1_ATM_H
