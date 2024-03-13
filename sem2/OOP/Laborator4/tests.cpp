#include <assert.h>
#include "tests.h"
#include "patrat.h"
#include "operations.h"
void testopp()
{
    Repo repo;
    Patrat p1(3,4,5);
    repo.add(p1);
    Patrat p2(20,7,8);
    Patrat p3(20,6,8);
    Patrat p4(20,5,7);
    Patrat p5(5,5,5);
    repo.add(p2);
    repo.add(p3);
    repo.add(p4);
    repo.add(p5);
    assert(cmm(repo)==20);
    assert(apcandran1(repo,0)==1);
    assert(apcandran1(repo,1)==0);
    int pozf=0,lmax=1;
    secventa(repo,pozf,lmax);
    assert(pozf==3);
    assert(lmax==3);

}
void testrepo()
{
    Repo repo;
    Patrat p1(3,4,5);
    repo.add(p1);
    Patrat p2(20,7,8);
    repo.add(p2);
    assert(repo.getSize()==2);
}
void test_domain()
{
    Patrat p(4,2,3);
    assert(p.get_perimetru()==16);
    assert(p.get_arie()==16);
    assert(p.get_lat()==4);
    assert(p.get_x()==2);
    assert(p.get_y()==3);
    p.set_lat(10);
    p.set_x(4);
    p.set_y(7);
    assert(p.get_y()==7);
    assert(p.get_x()==4);
    assert(p.get_perimetru()==40);
    assert(p.get_arie()==100);
    assert(p.get_lat()==10);
    p.~Patrat();
}
