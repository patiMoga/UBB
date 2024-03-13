#include "menu.h"
#include <iostream>
#include <cstdlib>
#include <ctime>
#include "atm.h"
using namespace std;

void generate_option(int suma, Atm atm, Collection& colectie){
    int i = 0;
    while(suma > 0){
        if(atm.get_colectie().get_elements()[i] <= suma && atm.get_colectie().get_occurences()[i] != 0){
            colectie.add(atm.get_colectie().get_elements()[i]);
            suma = suma - atm.get_colectie().get_elements()[i];
        }
        else i++;

    }
}
void savetransactions(int& n, Atm& atm){
    int id, suma;
    Collection colectie;
    Tranzactie* tranzactii;
    tranzactii = atm.get_alltransactions();
    cout << "Introduceti suma tranzactiei: ";
    cin >> suma;
    srand(time(0));
    id = rand() % 1000;
    generate_option(suma, atm, colectie);
    for(int j = 0; j < colectie.get_distinctelements() - 1; j++)
        cout << colectie.get_elements()[j] << "*" << colectie.get_occurences()[j] << " + ";
    cout << colectie.get_elements()[colectie.get_distinctelements() - 1] << "*" << colectie.get_occurences()[colectie.get_distinctelements() - 1];
    cout << endl <<  "Sunteti de acord cu aceasta modalitate de tranzactie ? " << endl;
    cout << " 1. DA" << endl << " 2. NU" << endl;
    cout << "Raspuns: ";
    int comanda;
    cin >> comanda;
    cout << endl;
    switch(comanda){
        case 1:
            tranzactii[n].set_id(id);
            tranzactii[n].set_suma(suma);
            tranzactii[n].set_collection(colectie);
            n++;
            break;
        case 2:
            cout << "Efectuati alte tranzactii:)" << endl;
            break;

    }


    atm.set_numartranzactii(n);
    atm.set_tranzactii(tranzactii);
}

void printtransactions(Atm atm, int n){
    for(int i = 0; i < n; i++) {
        cout << "Tranzactia numarul " << i + 1 << endl;
        cout << "ID: " << atm.get_alltransactions()[i].get_id() << " ; ";
        cout << "Suma: " << atm.get_alltransactions()[i].get_suma() << " ; ";
        cout << "Modalitate de plata: ";
        Collection colectie = atm.get_alltransactions()[i].get_collection();
        for(int j = 0; j < colectie.get_distinctelements() - 1; j++ ) {
            cout << colectie.get_elements()[j] << "*" << colectie.get_occurences()[j] << " + ";
        }
        cout << colectie.get_elements()[colectie.get_distinctelements() - 1] << "*" << colectie.get_occurences()[colectie.get_distinctelements() - 1];
        cout << endl;
    }
}
void options(){
    cout << "\n\nAlegeti o optiune: "<< endl;
    cout << "1. Efectueaza tranzactii" << endl;
    cout << "2. Afiseaza tranzactii" << endl;
    cout << "0.Exit"<< endl;
}

void run_menu(Collection colectie){
    int n  = 0;
    Tranzactie* tranzactii = new Tranzactie[20];
    bool value = true;
    Atm atm(tranzactii, colectie, n);
    while(value){
        options();
        int command;
        cout << "Comanda :";
        cin >> command ;
        switch (command) {
            case 1:
                savetransactions( n, atm);
                break;
            case 2:
                printtransactions(atm, n);
                break;
            default: {
                cout << "Goodbye!";
                value = false;
            }

        }
    }
}