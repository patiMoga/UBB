
#ifndef LAB_4_5_SD_V1_TRANZACTIE_H
#define LAB_4_5_SD_V1_TRANZACTIE_H

#include <bits//stdc++.h>
#include <tuple>
#include <vector>

using namespace std;
class Tranzactie {
private:
    int idTranzactie;
    int suma;
    vector<tuple<int, int>> modalitateDePlata;

public:
    Tranzactie();

    Tranzactie(int idTranzactieAtribuire, int sumaAtribuire, vector<tuple<int, int>> modalitateDePlata);

    ~Tranzactie();

    friend ostream &operator<<(ostream &os, Tranzactie &tranzactie);
};


#endif //LAB_4_5_SD_V1_TRANZACTIE_H
