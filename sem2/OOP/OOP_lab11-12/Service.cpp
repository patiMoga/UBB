
#include "Service.h"
#include "utils/MyException.h"
#include "utils/PurchesException.h"
#include<iostream>
#include <algorithm>
using namespace std;

Service::Service(Repo_tonomat &repo) {
    this->repo = &repo;
}

vector<Produse*> Service::get_all_produse() {
    return this->repo->get_all();
}

void Service::add_produs(int cod, string name, int pret) {
    bool ok = 0;
    vector<Produse*> produse = repo->get_all();
    for(int i= 0 ; i < produse.size() ; ++i){
        if(produse[i]->get_cod() == cod)
            ok = 1;
    }

    if(ok)
        throw MyCostumNumerException("Exista deja un produs cu codul dat!");
    if(pret < 0)
        throw MyCostumNumerException("Pretul nu poate fi negativ!");
    Produse *p = new Produse(cod, name, pret);
    this->repo->add_produs(*p);
}
void Service::delete_produs(int cod) {
    this->repo->delete_produs(cod);

}
bool cmpPrice(Produse *p1, Produse *p2){
    return (p1->get_pret() < p2->get_pret());
}
vector<Produse *> Service::sort_by_price() {
    vector<Produse*> produse = this->repo->get_all();
    std::sort(produse.begin(), produse.end(), cmpPrice);
    return produse;
}

vector<Produse*> Service::filter_by_price(int price) {
    vector<Produse*> produse = this->repo->get_all();
    vector<Produse*> result ;
    for(int i=0; i< produse.size() ; i++){
        if(produse[i]->get_pret() <=price)
            result.push_back(produse[i]);
    }
    return result;
}

void Service::add_bancnota(int tip_bancnota) {
    int v[8] = {1, 5, 10, 20, 50 , 100, 200, 500};
    for(int i = 0; i< 8 ; i++){
        if(tip_bancnota == v[i]){
            repo->add_bancnota(tip_bancnota);
        }
    }

}

void Service::delete_bancnota(int tip_bancnota) {
    int v[8] = {1, 5, 10, 20, 50 , 100, 200, 500};
    for(int i = 0; i< 8 ; i++){
        if(tip_bancnota == v[i]){
            repo->delete_bancnota(tip_bancnota);
        }
    }
}

bool Service::verificare_suma(int suma) {
    int exista = false;
    vector<int> bancnote = repo->get_all_bancnote();
    vector<int> aparitii = repo->get_all_aparitii();
    int size_bancnote = bancnote.size();
    int i = 0;
    while(i<size_bancnote && suma > 0){
        int bancnota = bancnote[i];
        int nr_aparitii = aparitii[i];
        while(nr_aparitii != 0 && suma >= bancnota){
            suma = suma - bancnota;
        }
        i++;
    }

    if(suma == 0)
        exista = true;

    return exista;
}

void Service::add_sum_to_vector(int sum) {
    int valori[8] = {500, 200, 100, 50, 20, 10 , 5, 1};
    int i = 0;
    while(i< 8 && sum > 0){
        int bancnota = valori[i];
        if(sum >= bancnota){
            repo->add_bancnota(bancnota);
            sum = sum - bancnota;
        }
        i++;
    }
}
void Service::delete_sum_from_vector(int sum) {
    int valori[8] = {500, 200, 100, 50, 20, 10 , 5, 1};
    int i = 0;
    while(i< 8 && sum > 0){
        int bancnota = valori[i];
        while(sum >= bancnota){
            repo->delete_bancnota(bancnota);
            sum = sum - bancnota;
        }
        i++;
    }

}

int Service::purchese(int sum, int cod) {
    vector<int> bancnote = repo->get_all_bancnote();
    vector<int> aparitii = repo->get_all_aparitii();
    vector<Produse *> produse = repo->get_all();
    Produse *produs;
    int rest;
    bool exist = false;
    if(bancnote.size() == 0){
        throw PurchesException("Fonduri insuficiente!");
    }
    for (int i = 0; i < produse.size(); i++) {
        if (produse[i]->get_cod() == cod) {
            exist = true;
            produs = produse[i];
        }
    }
    if(exist== false){
        throw MyCostumNumerException("Produsul nu exista!");
    }

    if (sum < produs->get_pret()) {
        throw PurchesException("Fonduri insuficiente!");}
    else{
        add_sum_to_vector(sum);
        rest = sum - produs->get_pret();
        if (verificare_suma(rest)) {
            delete_produs(cod);
            delete_sum_from_vector(rest);
            return rest;
        }
    }
}