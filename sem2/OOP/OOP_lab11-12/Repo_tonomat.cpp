
#include "Repo_tonomat.h"
#include "utils/MyException.h"

vector<Produse*> Repo_tonomat::get_all() {
    return this->produse;
}
void Repo_tonomat::add_produs(Produse &p){
    this->produse.push_back(&p);
}

void Repo_tonomat::delete_produs(int cod) {
    bool ok = 0;
    int size = produse.size();
    for (int i = 0; i < size; i++) {
        if (produse[i]->get_cod() == cod) {
            ok = 1;
            produse[i] = produse[i + 1];
        }
    }
    produse.resize(size - 1);

    if (ok == 0)
        throw MyCostumNumerException("Produsul nu exista!");
}

vector<int> Repo_tonomat::get_all_bancnote() {
    return bancnote;
}

void Repo_tonomat::add_bancnota(int tip_bancnota) {
    bool exista = false;
    int pos;
    for(int i = 0 ; i< bancnote.size() ; i++)
        if(bancnote[i] == tip_bancnota) {
            exista = true;
            pos = i;
        }

    if(exista)
        aparitii[pos] = aparitii.at(pos) + 1;
    else
    {
        bancnote.push_back(tip_bancnota);
        aparitii.push_back(1);
    }

}

void Repo_tonomat::delete_bancnota(int tip_bancnota) {
    bool exista = false;
    int poz = 0 ;
    for(int i = 0 ; i<bancnote.size() ; i++) {
        if (bancnote[i] == tip_bancnota) {
            exista = true;
            poz = i;
        }
    }

    if(exista){
        if(aparitii.at(poz) > 1)
            aparitii[poz] = aparitii.at(poz) - 1;
        else
        {
            bancnote.erase(bancnote.begin()+poz);
            aparitii.erase(aparitii.begin()+poz);
        }
    }

}