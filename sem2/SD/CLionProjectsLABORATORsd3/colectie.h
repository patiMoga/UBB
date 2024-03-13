#ifndef SDSEM2_COLECTIE_H
#define SDSEM2_COLECTIE_H
#include "vectordinamic.h"
typedef int TElem;

class Collection{
private:
    VectorDinamic elements;
    VectorDinamic occurrences;
    int distinctelements;
    int capacity;
    void redim();
public:
    Collection();
    void add(TElem elem);
    bool remove(TElem elem);
    bool search(TElem elem);
    int get_distinctelements();
    int noccurrences(TElem elem);
    ~Collection();
    int* get_elements();
    int* get_occurences();
};
#endif //SDSEM2_COLECTIE_H
