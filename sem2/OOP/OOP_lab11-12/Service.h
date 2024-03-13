
#ifndef OOP_LAB11_12_SERVICE_H
#define OOP_LAB11_12_SERVICE_H

#include "Produse.h"
#include"Repo_tonomat.h"

class Service {
private:
    Repo_tonomat *repo;
public:
    Service(Repo_tonomat &repo);

    vector<Produse*> get_all_produse();

    void add_produs(int cod, string name, int pret);

    void delete_produs(int cod);

    vector<Produse*> sort_by_price();

    vector<Produse*> filter_by_price(int price);

    vector<int> get_all_bancnote(){
        return repo->get_all_bancnote();
    }

    vector<int> get_all_aparitii(){
        return repo->get_all_aparitii();
    }

    void add_bancnota(int tip_bancnota);

    void delete_bancnota(int tip_bancnota);

    bool verificare_suma(int suma);

    void add_sum_to_vector(int sum);

    void delete_sum_from_vector(int sum);

    int purchese(int sum, int cod);

};


#endif //OOP_LAB11_12_SERVICE_H
