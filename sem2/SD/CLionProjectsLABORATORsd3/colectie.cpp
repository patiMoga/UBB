#include "colectie.h"
#include <iostream>
#include "vectordinamic.h"
using namespace std;
Collection::Collection() {
    this -> distinctelements = 0;
    this -> capacity = 500;
    this -> elements = VectorDinamic(capacity);
    this -> occurrences = VectorDinamic(capacity);
}

void Collection::add(TElem elem) {
    if (this->elements.search(elem)) {
        int poz = -1, i = 0;
        while ((poz == -1) && (i < this->elements.get_length()))
            if (this->elements.getAt(i) == elem)
                poz = i;
            else
                i++;
        int oc = this -> occurrences.getAt(poz) ;
        this -> occurrences.setAt(poz, oc + 1);

    } else {
        this->elements.add(elem);
        this -> occurrences.add(1);

    }
}
bool Collection::remove(TElem elem) {
    if(search(elem)) {
        int i = this->elements.getPosition(elem);
        this->elements.remove(i);
        this->occurrences.remove(i);
        return true;
    }
    return false;
}

bool Collection::search(TElem elem) {
    return this -> elements.search(elem);
}

int Collection::get_distinctelements() {
    return this -> elements.get_length();
}

int Collection::noccurrences(TElem elem) {
    int i = this -> elements.search(elem);
    return this -> occurrences.getAt(i);
}

Collection::~Collection() {

}

int *Collection::get_elements() {
    return this -> elements.get_elements();
}
int *Collection::get_occurences() {
    return this -> occurrences.get_elements();
}