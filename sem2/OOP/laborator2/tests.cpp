#include <iostream>
#include <assert.h>
#include "rezolv56.h"
#include "tests.h"
using namespace std;

void testeprim()
{
    assert(prim(0)==0);
    assert(prim(3)==1);
    assert(prim(56)==0);
    assert(prim(13)==1);
}

void testedif()
{
    int x[7]={2,5,7,5,12,4,8};
    int pozf=0;
    int lmax=0;
    dif(x,7,pozf,lmax);
    assert(pozf==4);
    assert(lmax=5);
}
void testeint()
{
    int x[10]={1,2,3,4,5,6,7,8,9,10};
    int pozf=0;
    int lmax=0;
    interval(x,10,2,6,pozf,lmax);
    assert(pozf==5);
    assert(lmax==5);
}
void teste()
{
    testedif();
    testeint();
    testeprim();
}