

#ifndef OOP_LAB11_12_FILEREPOSITORY_H
#define OOP_LAB11_12_FILEREPOSITORY_H

#pragma once
#include "Repo_tonomat.h"
#include <fstream>
#include "iostream"
using namespace std;


class FileRepository: public Repo_tonomat{
private:
    string file_name;
public:
    FileRepository(const string &file_name);
    void loadFromFile();
    void saveInFile();

    void add_produs(Produse &produs) override;
    void delete_produs(int cod) override;
    vector<Produse*> get_all() override;
    int get_current_size() override;

};


#endif //OOP_LAB11_12_FILEREPOSITORY_H
