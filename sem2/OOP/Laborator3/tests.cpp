#include <iostream>
#include <assert.h>
#include "tests.h"
#include "rezolvare.h"

void testsemnedif1()
{
    int *x=new int[7]{1,3,2,10,5,2,3};
    int pozf=2,lmax=2;
    semnedif(x,7,pozf,lmax);
    assert(pozf==4);
    assert(lmax=5);
    delete []x;
    x=NULL;

}
void testsemnedif2() {
    int *x =new int[7] {5, 3, 2, 10, 5, 20, 3};
    int pozf = 2, lmax = 2;
    semnedif(x, 7, pozf, lmax);
    assert(pozf == 6);
    assert(lmax == 6);
    delete []x;
    x=NULL;
}

void testedistincte1()
{
    int *x=new int[12]{2,3,4,5,2,4,6,7,8,9,10,2};
    int pozi=0;
    int pozf=0;
    distincte(x,12,pozi,pozf);
    assert(pozi==3);
    assert(pozf==10);
    delete []x;
    x=NULL;
}
void testedistincte2()
{
    int *x=new int[12]{1,3,4,5,2,10,6,7,1,9,10,2};
    int pozi=0;
    int pozf=0;
    distincte(x,12,pozi,pozf);
    assert(pozf==9);
    assert(pozi==1);
    delete []x;
    x=NULL;

}
void teste()
{
    testsemnedif1();
    testsemnedif2();
    testedistincte1();
    testedistincte2();
}
