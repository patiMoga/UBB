//
// Created by ARDELE on 5/30/2022.
//

#ifndef EXAMEN_PRACTIC_30_05_2022_UI_H
#define EXAMEN_PRACTIC_30_05_2022_UI_H
#include <string>
#include "Service.h"
using namespace std;


class UI {
private:
    Service& service;
public:
    UI(Service& service);
    ~UI();
    void RunMenu();
    void UIAddBacterie(std::string denumire, int varsta, std::string tip);
    void uishowall();
    void uiafisaredupatip(std::string tip);
    void uiafisaredupadurata(int timp);
    int uiafisarevarstamedie();
    static void DisplayMenu();

};


#endif //EXAMEN_PRACTIC_30_05_2022_UI_H
