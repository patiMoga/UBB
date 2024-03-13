

#ifndef OOP_LAB11_12_REPO_TONOMAT_H
#define OOP_LAB11_12_REPO_TONOMAT_H


#include "Produse.h"
#include <vector>
using namespace std;

class Repo_tonomat {
private:
    int currentSize = 0;
    vector<int> bancnote;
    vector<int> aparitii;
protected:
    vector<Produse*> produse;

public:
    Repo_tonomat() = default;
    ~Repo_tonomat() = default;
    virtual int get_current_size(){
        return currentSize;
    }
    virtual vector<Produse*> get_all();
    virtual void add_produs(Produse &p);
    virtual void delete_produs(int cod);
    vector<int> get_all_bancnote();
    vector<int> get_all_aparitii(){
        return aparitii;
    }
    void add_bancnota(int tip_bancnota);
    void delete_bancnota(int tip_bancnota);



};



#endif //OOP_LAB11_12_REPO_TONOMAT_H
