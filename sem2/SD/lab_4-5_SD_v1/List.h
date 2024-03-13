
#ifndef LAB_4_5_SD_V1_LIST_H
#define LAB_4_5_SD_V1_LIST_H
#include <iostream>
#include "Node.h"
using namespace std;

template <class T>
class List {
private:

    Node<T>* first;
    Node<T>* last;

public:
    List () {
        this->first = nullptr;
        this->last = nullptr;
    }

    int size() const;

    bool is_empty() const;

    void push_back(T e);


    void push_front(T e);

    T get_at(int i) const;

    T update(int i, T e);


    void set_at(int i, T e);

    T delete_at(int i);
    int search(T e)  const;

    List<T> getAll();

    List<T>& operator=(const List<T>& other);

    ~List();

};



template<class T>
List<T> &List<T>::operator=(const List<T> &other) {
    if (this != &other) {
        // curatam lista curenta
        while (first != nullptr) {
            Node<T>* temp = first;
            first = first->next;
            delete temp;
        }

        // facem o copie a elementelor din lista 'other' (deep copy)
        Node<T>* current = other.first;
        Node<T>* prev = nullptr;
        while (current != nullptr) {
            Node<T>* newNode = new Node<T>(current->info);
            if (prev == nullptr) {
                first = newNode;
            }
            else {
                prev->next = newNode;
                newNode->prev = prev;
            }
            prev = newNode;
            current = current->next;
        }
    }

    return *this;
}

template<class T>
List<T> List<T>::getAll() {
    List<T> result;

    Node<T>* crt = first;
    while(crt != nullptr)
    {
        result.push_back(crt->info);
        crt = crt->next;
    }

    return result;
}

template<class T>
void List<T>::push_front(T e) {
    auto newNode = new Node<T>(e);
    // daca lista este goala (first == nullptr, last == nullptr)
    if(first == nullptr)
    {
        first = newNode;
        last = newNode;
    }
    else{ // daca lista are deja elemente
        newNode->next = first;
        first->prev = newNode;
        first = newNode;
    }
}

template<class T>
List<T>::~List() {

    while(first != nullptr)
    {
        Node<T>* node = first;
        first = first->next;
        delete node;
    }
}

template<class T>
T List<T>::delete_at(int i) {
    if( i < 0 || i>= size())
        throw std::invalid_argument("Pozitia nu este valida!");

    int noElements = 0;
    Node<T>* crt = first;
    while(noElements < i)
    {
        noElements ++;
        crt = crt->next;
    }

    T e = crt->info;
    if(crt->prev != nullptr)
        crt->prev->next = crt->next;
    else
        first = crt->next;

    if(crt->next != nullptr)
        crt->next->prev = crt->prev;
    else
        last = crt->prev;

    delete crt;
    return e;



}

template<class T>
void List<T>::set_at(int i, T e) {
    if( i < 0 || i>= size())
        throw std::invalid_argument("Pozitia nu este valida!");

    Node<T>* newNode = new Node<T>(e);
    if(i == 0) // newNode vine in locul lui first
    {
        newNode->next = first;
        first->prev = newNode; // if(first != nullptr) ?
        first = newNode;
    }
    else
    {
        Node<T>* crt = first;
        int noELements = 0;
        while(noELements < i - 1)
        {
            crt = crt->next;
            noELements ++;
        }
        newNode->next = crt->next;
        newNode->prev = crt;
        crt->next->prev = newNode; // if(crt->next != nullptr) ?
        crt->next = newNode;
    }
}

template<class T>
int List<T>::search(T e) const { // done, la fel
    Node<T>* node = first;
    int contor = 0;
    while(node != nullptr)
    {
        if(node->info == e)
            return contor;
        node = node->next;
        contor++;
    }
    return -1;
}

template<class T>
T List<T>::update(int i, T e) { //done (la fel ca la lista simplu inlantuita)
    if(i < 0 || i >= size())
        throw invalid_argument("Pozitia e invalida!");
    Node<T>* crt = first;
    int noE = 0;
    while (noE < i){ // ca la get_at, ne ducem exact pe elem de pe pozitia i
        crt = crt->next;
        noE++;
    }
    T old_value = crt->info;
    crt->info = e;

    return old_value;
}

template<class T>
T List<T>::get_at(int i) const { // done (la fel ca la lista simplu inlantuita)
    if(i < 0 || i >= size())
        throw invalid_argument("Pozitia e invalida!");
    Node<T>* crt = first;
    int noE = 0;
    while (noE < i){ // ne ducem cu crt exact pe elem de pe pozitia i
        crt = crt->next;
        noE++;
    }
    return crt->info;
}

template<class T>
void List<T>::push_back(T e) { // done
    Node<T>* newNode = new Node<T>(e);
    if(first == nullptr){
        first = newNode;
        last = newNode;
    }
    else{
        newNode->prev = last;
        last->next = newNode;
        last = newNode;
    }

}

template<class T>
bool List<T>::is_empty() const {
    return first == nullptr;
}

template<class T>
int List<T>::size() const { // done
    int contor = 0;
    Node<T>* last = first;
    while(last != nullptr)
    {
        contor++;
        last = last->next;
    }
    return contor;
}

#endif //LAB_4_5_SD_V1_LIST_H
