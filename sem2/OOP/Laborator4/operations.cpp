#include "operations.h"
#include "repository.h"
#include "patrat.h"
int cmm(Repo repo)
{
    int n=repo.getSize(),max=0,pm=0;
    for(int i=0;i<n;i++)
        if(repo.getbyPos(i).get_arie()>max)
        {
            max=repo.getbyPos(i).get_arie();
            pm=i;
        }
    return repo.getbyPos(pm).get_lat();
}
int apcandran1(Repo repo,int pos)
{
    int j=repo.getbyPos(pos).get_lat()/2;
    int a=repo.getbyPos(pos).get_x()-j;
    int b=repo.getbyPos(pos).get_y()-j;
    if(a>=0&&b>=0)
        return 1;
    return 0;
}
void secventa(Repo repo,int &pozf,int &lmax)
{
    int l=1;
    Patrat p;
    p=repo.getbyPos(0);
    for(int i=1;i<repo.getSize();i++)
    {
        if(p.get_lat()==repo.getbyPos(i).get_lat())
        {
            l++;
            if(l>lmax)
            {
                lmax=l;
                pozf=i;
            }
        }
        else
            l=1;
        p=repo.getbyPos(i);
    }
}