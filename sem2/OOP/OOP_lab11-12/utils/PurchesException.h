

#ifndef OOP_LAB11_12_PURCHESEXCEPTION_H
#define OOP_LAB11_12_PURCHESEXCEPTION_H

#include <iostream>
#include <string>
using namespace std;


class PurchesException: public exception{
private:
    string message;
public:
    PurchesException(string message):message(message){};

    const char* what() const noexcept override{
        return "Fonduri insuficente!";
    }

};


#endif //OOP_LAB11_12_PURCHESEXCEPTION_H
