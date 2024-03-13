//
// Created by ARDELE on 5/30/2022.
//

#ifndef EXAMEN_PRACTIC_30_05_2022_BACTERIE_H
#define EXAMEN_PRACTIC_30_05_2022_BACTERIE_H
#include "iostream"
#include "string"

class Bacterie {
private:
    std::string denumire;
    int varsta;
    std::string tip;
public:
    Bacterie();
    Bacterie(std::string denumire,int varsta, std::string tip);
    Bacterie(const Bacterie &b);
    ~Bacterie();
    Bacterie operator =(const Bacterie &b);

    std::string getnume();
    int getvarsta();
    std::string gettip();


    void setdenumire(std::string denumire);
    void setxa(int varsta);
    void settip(std::string tip);



};


#endif //EXAMEN_PRACTIC_30_05_2022_BACTERIE_H
