

#ifndef OOP_LAB11_12_FILEEXCEPTION_H
#define OOP_LAB11_12_FILEEXCEPTION_H
#include<iostream>
using namespace std;

class FileException:public exception {
public:
    const char* what() const noexcept override{
        return "The file can be open!";
    }
};


#endif //OOP_LAB11_12_FILEEXCEPTION_H
