
#include "FileRepository.h"
#include "utils/FileException.h"

FileRepository::FileRepository(const string &file_name): file_name(file_name) {
    loadFromFile();
}

void FileRepository::loadFromFile() {
    ifstream f(file_name);

    if (!f.is_open()){
        throw FileException();
    }

    produse.clear();

    while (!f.eof()){
        int cod, pret;
        string name;

        while( f >> cod >> name >> pret){
            Produse product = Produse(cod, name, pret);
            Produse *p = new Produse(product);
            this->produse.push_back(p);
        }
    }
    f.close();
}

void FileRepository::saveInFile() {
    ofstream file(file_name);

    if (!file.is_open()){
        cout<<"Fisierul nu a putut fi deschis!";
        return;
    }

    for (const auto &p: Repo_tonomat :: get_all()){
        file<<p->get_cod()<<" "<<p->get_name()<<" "<<p->get_pret()<<endl;
    }
    file.close();
}

void FileRepository::add_produs(Produse &produs) {
    Repo_tonomat::add_produs(produs);
    saveInFile();
}
void FileRepository::delete_produs(int cod) {
    Repo_tonomat::delete_produs(cod);
    saveInFile();
}

vector<Produse*> FileRepository::get_all() {
    loadFromFile();
    return produse;
}

int FileRepository::get_current_size() {
    loadFromFile();
    return Repo_tonomat::get_current_size();
}
