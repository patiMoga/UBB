
#include "ATM.h"

void ATM::printMenu() {
    cout << endl;
    cout << "0.Exit" << endl;
    cout << "1. Afiseaza colectia de bancnote" << endl;
    cout << "2. Afiseaza toate tranzactiile" << endl;
    cout << "3. Plateste" << endl;
    cout << "Alege o optiune: ";
}

void ATM::afisareColectie() {
    colectie.saveToFile("colectie.txt");
    List<int> bancnote = colectie.getAll();
    List<int> occs = colectie.getAparitii();

    cout << "Colectia de bancnote este:" << endl;
    for(int i = 0; i < colectie.dim(); i++)
    cout << bancnote.get_at(i) << " : " << occs.get_at(i) << endl;
}

void ATM::plateste() {
    //colectie.saveToFile("colectie.txt");
    int sumaCareTrebuiePlatita;

    cout << "Introduceti suma care trebuie platita:";
    cin >> sumaCareTrebuiePlatita;

    List<int> bancnote = colectie.getAll();
    List<int> occur_bancnote = colectie.getAparitii();

    int sizeBancnote = colectie.dim();

    vector<tuple<int, int>> tupluri;

    int suma = 0;
    int id;
    for (int i = 0; i < sizeBancnote; i++) {
        int nrBancnoteFolosite = 0;
        if (occur_bancnote.get_at(i) > 0) {
            while (suma + bancnote.get_at(i) <= sumaCareTrebuiePlatita && occur_bancnote.get_at(i) > 0)
            {
                suma += bancnote.get_at(i);
                nrBancnoteFolosite++;
                //colectie.modificaAparitii(colectie.getBancnota(i), 1);
                occur_bancnote.update(i, occur_bancnote.get_at(i) - 1);
            }
            std::tuple<int,int> tupp = make_tuple(bancnote.get_at(i), nrBancnoteFolosite);
            tupluri.push_back(tupp);
        }
    }
    if(suma < sumaCareTrebuiePlatita || suma > sumaCareTrebuiePlatita)
        cout << "Suma introdusa de dvs nu poate fi procesata!" << endl;
    else{
        cout << "Suma dvs se poate procesa. Doriti sa continuati?" << endl;

        string decizie;
        cin >> decizie;
        if(decizie == "da")
        {
            id = tranzactii.size() + 1;
            Tranzactie tranzactie(id, sumaCareTrebuiePlatita, tupluri);
            tranzactii.push_back(tranzactie);
            colectie.setNewOccs(occur_bancnote);
            //colectie.setNewOccs_2(occur_bancnote);
            colectie.saveToFile("colectie.txt");
            cout << tranzactie;
        }
        else if(decizie == "nu")
            cout << "OK..." << endl;
    }
}

void ATM::showTranzactii() {
//    for(int i = 0; i < tranzactii.size(); i++)
//        cout << tranzactii[i] << endl;
    for(auto& tranzactie : tranzactii)
        cout << tranzactie << endl;
}

void ATM::runATM() {
    while(true)
    {
        printMenu();
        char opt;
        cin >> opt;
        cout << endl;

        if (opt == '1') {
            afisareColectie();
        }
        else if (opt == '2')
        {
            showTranzactii();
        }
        else if(opt == '3')
        {
            plateste();
        }
        else if(opt == '0')
        {
            std::cout<<"Buh Bye!";
            exit(0);

        }
    }
}


