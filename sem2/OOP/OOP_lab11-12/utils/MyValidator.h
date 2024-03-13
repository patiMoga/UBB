
#ifndef OOP_LAB11_12_MYVALIDATOR_H
#define OOP_LAB11_12_MYVALIDATOR_H
#include <iostream>
#include <string>
#include <sstream>
#include "ValidatorError.h"
using namespace std;

class MyValidator {
public:
    static int isNumer(string possible_number){
        try{
            return stoi(possible_number);
        }catch (exception e){
            throw ValidatorError("Recived parameter is not a int!");
        }
    }


};


#endif //OOP_LAB11_12_MYVALIDATOR_H
