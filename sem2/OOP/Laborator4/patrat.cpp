#include "patrat.h"
//fara pam
Patrat::Patrat()
{
    this->latura=0;
    this->xc=0;
    this->yc=0;
}
//cu param
Patrat::Patrat(int a,int x,int y)
{
    this->latura=a;
    this->xc=x;
    this->yc=y;
}
//const
Patrat::Patrat(const Patrat &p)
{
    this->latura=p.latura;
    this->xc=p.xc;
    this->yc=p.yc;
}

//destr
Patrat::~Patrat(){}
//get
int Patrat::get_lat()
{
    return this->latura;
}
int Patrat::get_x()
{
    return this->xc;
}
int Patrat::get_y()
{
    return this->yc;
}
void Patrat::set_x(int x)
{
    this->xc=x;
}
void Patrat::set_y(int y)
{
    this->yc=y;
}
//set
void Patrat::set_lat(int a) {
    this->latura = a;
}
//aria
int Patrat::get_arie()
{   int a;
    a=this->latura*this->latura;
    return a;

}
//perimetru
int Patrat::get_perimetru()
{
    int p;
    p =this->latura;
    return p*4;
}