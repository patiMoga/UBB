
#ifndef OOP_LAB11_12_VALIDATORERROR_H
#define OOP_LAB11_12_VALIDATORERROR_H
#include<string>
using namespace std;
#include <iostream>

class ValidatorError: public exception{
private:
    string message;
public:
    ValidatorError(string messages): message(messages){}

    const char *what() const noexcept override{
        return message.c_str();
    }

};


#endif //OOP_LAB11_12_VALIDATORERROR_H