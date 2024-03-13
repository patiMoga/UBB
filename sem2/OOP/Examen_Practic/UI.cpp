//
// Created by ARDELE on 5/30/2022.
//

#include "UI.h"

UI::UI(Service &service) :service(service)
{///construnctor

}

UI::~UI() = default;

void UI::RunMenu() {
///functia de rulare a meniului
    int optiune;
    do {
        DisplayMenu();
        cout << "Introduceti optiunea: ";
        cin >> optiune;
        switch (optiune) {
            case 1:
            {
                cout << "Introduceti numele bacteriei:";
                string nume;
                cin>>nume;

                cout << "Introduceti varsta bacteriei:";
                int varsta;
                cin >> varsta;
                if (varsta<0) {cout<<"Varsta nu este introdusa corect!!!"<<endl;break;}

                cout << "Introduceti tipul bacteriei(tip1 sau tip2) :";
                string tip;
                cin>>tip;
//                if (tip!="tip1"|| tip!="tip2") {cout<<"Tipul nu este introdus corect!!!"<<endl;break;}

                this->UIAddBacterie(nume, varsta, tip);
                break;
            }

            case 2: {
                cout << "Lista Dreptelor: "<<endl;
                this->uishowall();
                break;
            }
            case 3: {
                cout << "Introduceti tipul"<<endl;
//                this->uiidentice(); m = (y2-y1)/(x2-x1);
//                this->uiperpendiculare();
                cout << "Introduceti tipul bacteriei(tip1 sau tip2) :";
                string tip;
                cin>>tip;
//                if (tip!="tip1"|| tip!="tip2") {cout<<"Tipul nu este introdus corect!!!"<<endl;break;}
                this->uiafisaredupatip(tip);
                break;

            }
            case 4: {
                cout << "Introduceti durata:";
                int timp;
                cin >> timp;
                if (timp<0) {cout<<"Timpul nu este introdus corect!!!"<<endl;break;}
                this->uiafisaredupadurata(timp);

                break;
            }
            case 5: {
                cout << "Media de varsta este:"<<endl;
                int varsta = this->uiafisarevarstamedie();
                cout << varsta<<endl;

                break;
            }
        }
    } while (optiune != 0);
}

void UI::UIAddBacterie(std::string denumire, int varsta, std::string tip) {
    ///functia de add din ui
    /// \param denumire: numele bacteriei
    /// \param vasrta: varsata bacteriei
    /// \param tip: tipul bacteriei
    this->service.AddElement(denumire,varsta, tip);
}

void UI::uishowall() {
///functia care afisaza toate entitatile
    this->service.showall();
}

void UI::uiafisaredupatip(std::string tip) {
    this->service.afisaredupatipulbacteriei(tip);
}

void UI::uiafisaredupadurata(int timp) {
    this->service.afisaredupatimp(timp);
}

int UI::uiafisarevarstamedie() {
    return this->service.mediadevarsta();
}

void UI::DisplayMenu() {
    cout <<"-----------------------------------------------------------------------"<<endl;
    cout << "1. Adauga Bacterie." << endl;
    cout << "2. Afisare Bacteriile." << endl;
    cout << "3. Afisare dupa tip." << endl;
    cout << "4. Afisareadupa un interval de timp." << endl;
    cout << "5. Media de varsta." << endl;
    cout << "0. Inchidere program." << endl;
    cout <<"-----------------------------------------------------------------------"<<endl;

}

