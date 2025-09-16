#ifndef START_COND_H
#define START_COND_H

#include "global_var.h"

//Задание н.у. условий для системы частиц

//Функция для задания н.у. двух частиц:
void start_cond_two_particles() {
    // Номер Варианта
    const double n = 19;
    // Частица 1
    coordx[0] = 0.75; coordy[0] = 0.25; coordz[0] = 0.75;
    // Частица 2
    coordx[1] = 1.25; coordy[1] = 0.25; coordz[1] = 0.75;

    // Скорость 1 частицы
    vx[0] = pow(2, 1.0 / n); vy[0] = 1.0; vz[0] = 0.0;
    // Скорость 2 частицы
    vx[1] = -pow(2, 1.0 / n); vy[1] = 1.0; vz[1] = 0.0;
}

#endif // START_COND_H
