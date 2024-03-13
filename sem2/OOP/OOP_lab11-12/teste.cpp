

#include "teste.h"
#include "Produse.h"
#include "Repo_tonomat.h"
#include "Service.h"
#include <cassert>


void test_produs(){
    Produse p(234, "milka", 10);
    Produse p1(621 , "Haribo" , 21);
    assert(p.get_cod() == 234);
    assert(p1.get_pret() == 21);
}

void test_repo_tonomat(){
    Repo_tonomat repo;
    Produse p(234, "milka", 10);
    Produse p1(621 , "Haribo" , 21);
    assert(repo.get_all().size() == 0);

    repo.add_produs(p);
    repo.add_produs(p1);
    vector<Produse*> produse = repo.get_all();

    assert(produse.size() == 2);
    assert(produse[0]->get_pret() == 10);
    assert(produse[1]->get_name() == "Haribo");
}

void test_service_tonomat(){
    Repo_tonomat repo;
    Service service(repo);
    service.add_produs(234, "milka", 10);
    service.add_produs(621 , "Haribo" , 21);
    service.add_produs(567, "CocCola" , 65);

    assert(service.get_all_produse().size() == 3);
    vector<Produse*> produse = service.get_all_produse();
    assert(produse[0]->get_pret() == 10);
    assert(produse[1]->get_name() == "Haribo");
    assert(produse[2]->get_cod() == 567);
    /// test sort
    service.sort_by_price();
    assert(produse[0]->get_pret() == 10);
    assert(produse[1]->get_pret() == 21);
    assert(produse[2]->get_cod() == 567);
    /// test filter
    vector<Produse*>result = service.filter_by_price(25);
    assert(result[0]->get_pret() == 10);
    assert(result[1]->get_pret() == 21);

    vector<int> bancnote = service.get_all_bancnote();
    vector<int> aparitii = service.get_all_aparitii();
    service.add_bancnota(5);
    service.add_bancnota(5);
    service.add_bancnota(5);
    service.add_bancnota(5);
    service.add_bancnota(5);
    service.add_bancnota(10);
    int rest = service.purchese(10,234);
    assert(rest == 0);






}

void test_all(){
    test_produs();
    test_repo_tonomat();
    test_service_tonomat();
}