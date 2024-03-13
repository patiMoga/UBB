
#ifndef LAB_4_5_SD_V1_COLECTIE_H
#define LAB_4_5_SD_V1_COLECTIE_H

#include "Node.h"
#include "List.h"

class Colectie {
private:
    List<int> nums;
    List<int> counts;
    std::string filename;

public:
    Colectie(); // poate aici ne putem initializa colectia...
    ~Colectie();
    void adauga(int num, int occ);
    int cauta(int num);
    void setNewOccs(const List<int>& someList);
    List<int> setNewOccs_2(const List<int>& someList);
    int dim();
    List<int> getAll();
    List<int> getAparitii();

    void loadFromFile(const std::string& filename);
    void saveToFile(const std::string& filename);
};


#endif //LAB_4_5_SD_V1_COLECTIE_H
