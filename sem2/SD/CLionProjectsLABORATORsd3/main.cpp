#include "menu.h"
#include "colectie.h"
using namespace std;
void alimentare(Collection& colectie){
    colectie.add(500);
    colectie.add(200);
    colectie.add(100);
    colectie.add(50);
    colectie.add(20);
    colectie.add(10);
    colectie.add(5);
    colectie.add(1);
}
int main() {
    Collection colectie;
    for(int i = 0; i < 50; i++){
        alimentare(colectie);
    }
    run_menu(colectie);
    return 0;
}
