

#ifndef OOP_LAB11_12_UI_H
#define OOP_LAB11_12_UI_H


#include "Produse.h"
#include "Repo_tonomat.h"
#include "Service.h"
#include "utils/MyValidator.h"

class UI {
private:
    Service *service;

    void print_menu();

    void afisare();

    void afisare_bancnote();

public:
    UI(Service &service);

    void menu();

    void add_produs();

    void delete_produs();

    void sort_by_price();

    void filter_by_price();

    void add_bancnote_automat();

    void add_bancnota();

    void delete_bancnota();

    void verifica_suma();

    void add_bancnota_to_vector();

    void delete_bancnota_from_vector();

    void purchese();

};



#endif //OOP_LAB11_12_UI_H
