
#ifndef OOP_LAB11_12_MYEXCEPTION_H
#define OOP_LAB11_12_MYEXCEPTION_H
#include <iostream>
#include <string>
using namespace std;

class MyCostumNumerException: public exception{
private:
    string message;
public:
    MyCostumNumerException(string messages): message(messages){}

    const char *what() const noexcept override{
        return message.c_str();
    }
};



#endif //OOP_LAB11_12_MYEXCEPTION_H
