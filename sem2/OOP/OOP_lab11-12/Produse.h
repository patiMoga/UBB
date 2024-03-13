

#ifndef OOP_LAB11_12_PRODUSE_H
#define OOP_LAB11_12_PRODUSE_H


#include <iostream>
using namespace std;

class Produse {
private:
    int cod;
    string nume;
    int pret;
public:
    Produse() = default;
    Produse(int cod, string name, int pret);
    bool operator==(const Produse &produs);
    int get_cod(){
        return cod;
    }
    const string &get_name() const{
        return nume;
    }
    int get_pret(){
        return pret;
    }

    void set_cod(int cod){
        this->cod = cod;
    }

    void set_nume( string name){
        this->nume = name;
    }
    void set_pret(int pret){
        this->pret = pret;
    }

    ~Produse() = default;


};


#endif //OOP_LAB11_12_PRODUSE_H
