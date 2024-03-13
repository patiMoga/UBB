
#include "Colectie.h"
#include <fstream>
#include <sstream>
Colectie::Colectie()
{
    //loadFromFile("colectie.txt");
//    adauga(200, 2);
//    adauga(100, 5);
//    adauga(50,10);
//    adauga(10,50);
    std::ifstream file("colectie.txt");
    if(!file)
    {
        std::cerr << "Nu s a deschis fisierul pt citire..." << endl;
        return;
    }
    int num, count;
    while(file >> num >> count)
    {
        adauga(num, count);
    }
    file.close();
}

void Colectie::adauga(int num, int occ) {
    // int index = cauta(num) cumva, daca num exista deja, ii adaugam occ la occurrence-u lui
    nums.push_back(num);
    counts.push_back(occ);
}

int Colectie::cauta(int num) {
    for(int i = 0; i < nums.size(); i++)
        if(nums.get_at(i) == num)
            return i;
    return -1;
}

int Colectie::dim() {
    return nums.size();
}

List<int> Colectie::getAll() {
    return nums.getAll();
}

List<int> Colectie::getAparitii() {
    return counts.getAll();
}

void Colectie::setNewOccs(const List<int>& someList) {
    counts = someList; // trebuie implementat operator= in clasa List pt a se modifica counts, si ca sa dea exit code 0
//    for(int i = 0; i < someList.size(); i++)
//        counts.update(i, someList.get_at(i));
}

List<int> Colectie::setNewOccs_2(const List<int> &someList) {
    //counts = someList;
    for(int i = 0; i < someList.size(); i++)
        counts.update(i, someList.get_at(i));
    saveToFile("colectie.txt");
    return counts;
}

void Colectie::loadFromFile(const std::string& filename) {
   ifstream file(filename);
   if(!file.is_open())
       return;

   while(!file.eof())
   {
       int num, occ;
       while(file >> num >> occ)
       {
           nums.push_back(num);
           counts.push_back(occ);
       }
   }
   file.close();
}

void Colectie::saveToFile(const std::string& filename) {
    std::ofstream file(filename);
    if(!file)
    {
        throw std::runtime_error("Nu s-a putut deschide fisierul pt scriere");
    }
    for(int i = 0; i < nums.size(); i++)
        file << nums.get_at(i) << " " <<  counts.get_at(i) << endl;

    file.close();
}

Colectie::~Colectie() {
    saveToFile("colectie.txt");
}
