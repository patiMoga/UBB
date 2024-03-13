//
// Created by ARDELE on 5/30/2022.
//

#include "tests.h"
#include "tests.h"
//#include "Entitate.h"
#include "Service.h"
#include "Repository.h"
#include "cassert"
#include "iostream"
void tests() {
    Repository r;
    assert(r.getnoelem() == 0);
    Service s;
    Bacterie b1("nume1", 1, "tip1");
    r.addElem(b1);
    Bacterie b2("nume2", 2, "tip2");
    r.addElem(b2);
    Bacterie b3("nume3", 3, "tip1");
    r.addElem(b3);
    Bacterie b4("nume4", 4, "tip2");
    r.addElem(b4);
    Bacterie b5("nume5", 5, "tip1");
    r.addElem(b5);
    Bacterie b6("nume6", 6, "tip2");
    r.addElem(b6);
    Bacterie b7("nume7", 7, "tip1");
    r.addElem(b7);
    assert(r.getnoelem() == 7);
    //std::cout<<s.mediadevarsta();
    //assert(s.mediadevarsta()==4);
}
