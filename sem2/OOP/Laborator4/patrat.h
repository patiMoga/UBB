//
// Created by Andrei2 on 3/20/2023.
//

#ifndef LABORATOR4_PATRAT_H
#define LABORATOR4_PATRAT_H
class Patrat
{
private:
    int latura;
    int xc;
    int yc;
public:
    Patrat();
    Patrat(int a,int x,int y);
    Patrat(const Patrat &p);

    ~Patrat();
    int get_lat();
    int get_x();
    int get_y();
    void set_x(int x);
    void set_y(int y);
    void set_lat(int a);
    int get_arie();
    int get_perimetru();

};

#endif //LABORATOR4_PATRAT_H
