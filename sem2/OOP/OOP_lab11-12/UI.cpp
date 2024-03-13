

#include "UI.h"
#include "utils/MyException.h"
#include "utils/ValidatorError.h"
#include "utils/PurchesException.h"
#include "utils/FileException.h"
#include <iostream>
using namespace std;

UI::UI(Service &service) {
    this->service = &service;
}

void UI::afisare() {
    vector<Produse*> produse = this->service->get_all_produse();
    if(produse.empty()){
        cout<<"Tonomatul nu are produse!\n";
    }

    for(int i = 0 ; i< produse.size() ; i++){
        cout<<"Produs:" << "cod: " << produse[i]->get_cod() << " ,denumire: " << produse[i]->get_name() << " ,pret: " << produse[i]->get_pret() <<endl;
    }

}

void UI::add_produs() {
    try{
        string cod_raw;
        cout<<"Alegeti codul produsului introdus: \n";
        cin>>cod_raw;
        string name;
        cout<<"Introduceti denumirea produsului: \n";
        cin>>name;
        string pret_raw;
        cout<<"Pretul produsului este: \n";
        cin>>pret_raw;
        int cod = MyValidator::isNumer(cod_raw);
        int pret= MyValidator::isNumer(pret_raw);
        this->service->add_produs(cod,name,pret);}
    catch (ValidatorError &exc){
        cout<<"Exception: " << exc.what()<<endl;
    }
    catch (MyCostumNumerException &exc){
        cout<<"Exception: " << exc.what()<<endl;
    }
}

void UI::delete_produs() {
    try {
        string cod;
        cout << "Introduceti codul produsului de sters: \n";
        cin >> cod;
        int cod_bun = MyValidator::isNumer(cod);
        this->service->delete_produs(cod_bun);
    }
    catch (ValidatorError &exc){
        cout<<"Exception: " << exc.what()<<endl;
    }
    catch (MyCostumNumerException &e){
        cout<<"Exception: " << e.what()<<endl;
    }
}

void UI::sort_by_price() {
    for (const auto produs: this->service->sort_by_price()){
        cout<<"Produs:" << "cod: " << produs->get_cod() << " ,denumire: " << produs->get_name() << " ,pret: " << produs->get_pret() <<endl;
    }
}

void UI::filter_by_price() {
    try{
    string price;
    cout<<"Alegeti pretul dupa care sa se faca filtrarea: ";
    cin>> price;
    int price_ok = MyValidator::isNumer(price);
    for(const auto produs: service->filter_by_price(price_ok)) {
        cout << "Produs:" << "cod: " << produs->get_cod() << " ,denumire: " << produs->get_name() << " ,pret: "
             << produs->get_pret() << endl;
    }
    }catch(ValidatorError &mess){
        cout<<mess.what()<<endl;
    }
}

void UI::afisare_bancnote() {
    vector<int> bancnote = service->get_all_bancnote();
    vector<int> aparitii = service->get_all_aparitii();
    //cout<< bancnote.size();
    if(bancnote.size() == 0 ){
        cout<<" nu sunt bancnote!\n";
    }
    for(int i = 0 ; i< bancnote.size() ; i++)
        cout<<"bancnota: "<< bancnote[i] << " este in " << aparitii[i]<< " exemplare.\n";
}

void UI::add_bancnote_automat() {
    int v[8] = {500, 200, 100, 50, 20 , 10, 5, 1};
    for(int i = 0 ; i < 5 ; i++){
        for(int j = 0 ; j < 8 ; j++)
            service->add_bancnota(v[j]);
    }
}

void UI::add_bancnota(){
    int tip_bancnota;
    cout<<"Bancnota introdusa este: ";
    cin>> tip_bancnota;
    service->add_bancnota(tip_bancnota);

}

void UI::purchese() {

    try {
        string sum;
        cout << "Introduceti bancnota: ";
        cin >> sum;
        int sum_ok = MyValidator::isNumer(sum);
        cout << endl;
        string cod;
        int cod_ok = MyValidator::isNumer(cod);
        cout << "Alegeti codul produsului dorit: ";
        cin >> cod;
        int result = service->purchese(sum_ok, cod_ok);
        cout << "restul: " << result << endl;
    }catch (PurchesException &exc){
        cout<<"Exception: " << exc.what()<<endl;
    }catch (MyCostumNumerException &exc){
        cout<<"Exception: " << exc.what()<<endl;
    }
}

void UI::print_menu() {

    cout<<"1. Afiseaza produse din produse.\n";
    cout<<"2. Adauga produs in produse.\n";
    cout<<"3. Delete product.\n";
    cout<<"4. Sort products by price\n";
    cout<<"5. Afiseaza toate produsele cu pretul <= decat pretul dat.\n";
    cout<<"6. Afiseaza bancnote.\n";
    cout<<"7. Add bancnote_automat.\n";
    cout<<"8. Purchese\n";
    cout<<"0. Iesire\n";

}
void UI::menu() {
        while (true) {
            try {
            print_menu();
            string opt_old;
            cout << "Alege optiunea: ";
            cin >> opt_old;
            int opt = MyValidator::isNumer(opt_old);
            if (opt == 1) {
                this->afisare();
            } else if (opt == 2) {
                this->add_produs();
            } else if (opt == 3) {
                this->delete_produs();
            } else if (opt == 4) {
                this->sort_by_price();
            } else if (opt == 5) {
                this->filter_by_price();
            } else if (opt == 6) {
                this->afisare_bancnote();
            } else if (opt == 7) {
                this->add_bancnote_automat();
            }else if(opt == 8){
                this->purchese();
            }else if (opt == 0)
                break;
            else
                cout << "Optiune gresita!Reincercati!\n";
    }catch (ValidatorError &e){
        cout<<"Error: "<< e.what() << endl;
    }catch (FileException &ex){
                cout<<"error: " << ex.what()<<endl;
            }
        }
}