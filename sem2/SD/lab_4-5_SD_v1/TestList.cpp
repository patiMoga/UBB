
#include "TestList.h"

#include <iostream>
#include "List.h"
#include <assert.h>
void teste(){

    List<int> myList;


    myList.push_back(5);
    myList.push_back(10);
    myList.push_back(15);


    myList.push_front(2);
    myList.push_front(1);

    assert(myList.size()==5);


   assert(myList.get_at(2)==5);

    myList.update(2, 8);
    assert(myList.get_at(2)==8);


    myList.set_at(3, 12);
    assert(myList.get_at(3)==12);


    int deletedElement = myList.delete_at(1);

    assert(deletedElement==2);


    int index = myList.search(10);

    assert(index==3);


    List<int> newList = myList.getAll();
    std::cout << "Elemente:  ";
    for (int i = 0; i < newList.size(); i++) {
        std::cout << newList.get_at(i) << " ";
    }
    std::cout << std::endl;
    std::cout<<"Teste trecute cu brio!"<<std::endl<<std::endl<<std::endl;

}