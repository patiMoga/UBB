//
// Created by ARDELE on 5/30/2022.
//

#ifndef EXAMEN_PRACTIC_30_05_2022_UTILS_H
#define EXAMEN_PRACTIC_30_05_2022_UTILS_H
#include "Service.h"
#include "Repository.h"

void inmemorie()
{
    Repository repo;
    Service service(repo);

    service.AddElement("AB",1,"tip1");
    service.AddElement("DE",2,"tip1");
    service.AddElement("GH",3,"tip2");
    service.AddElement("JK",4,"tip1");
    service.AddElement("MN",5,"tip2");

    UI ui(service);

    ui.RunMenu();
}
#endif //EXAMEN_PRACTIC_30_05_2022_UTILS_H
