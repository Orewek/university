#include <iostream>
#include <fstream>
// Подключение заголовочных файлов 
#include "params.h" 
#include "constants.h" 
#include "global_var.h" 
#include "start_cond.h" 
#include <iomanip> 
#include <cstdio> 

//Модуль радиус-вектора между i-ой и j-ой частицами
// Расчет расстояния
double r_abs(double dx, double dy, double dz) {
    return sqrt(dx * dx + dy * dy + dz * dz);
}

//Вычисление потенциальной энергии взаимодействия и силы взаимодействия
// Потенциал Леннард-Джонса
void calculate_U_F(double r) {
        double SIGMA_r = SIGMA / r;

        // Номер Варианта
        const double n = 19;
        /*
        Потенциал Леннард-Джонса
        Значение потенциала на радиусе обрезания - используется для сдвига потенциала чтобы он плавно обрезался до нуля
        U(r) = 4ε[(σ/r)¹² - (σ/r)⁶]
        ε (EPS) - глубина потенциальной ямы
        σ (SIGMA) - расстояние, где потенциал = 0
        r - расстояние между частицами
        */
        U = 4 * EPS * (pow(SIGMA_r, n + 9) - pow(SIGMA_r, 6)) - UCUT;
        /*
        Потенциал Леннард-Джонса U(r) = 4ε[(σ/r)¹² - (σ/r)⁶]
        Сила - это производная потенциала по расстоянию со знаком минус F(r) = -dU/dr
        
        U(r) = 4ε[σ¹²/r¹² - σ⁶/r⁶]
        Найдем производную dU/dr = 4ε[ -12σ¹²/r¹³ + 6σ⁶/r⁷ ]
        
        Умножим на -1 чтобы получить силу F(r) = -dU/dr = 4ε[ 12σ¹²/r¹³ - 6σ⁶/r⁷ ]
        F(r) = 24ε[ (2σ¹²/r¹³) - (σ⁶/r⁷) ] / 2
        F(r) = 24ε/r * [ (2σ¹²/r¹²) - (σ⁶/r⁶) ]

        Введем замену SIGMA_r = σ/r
        F(r) = 24ε/r * [ 2(σ/r)¹² - (σ/r)⁶ ]
        F(r) = 24ε/r * [ 2(SIGMA_r)¹² - (SIGMA_r)⁶ ]

        Физический смысл F = 24 * EPS / r * (2 * pow(SIGMA_r, 12) - pow(SIGMA_r, 6))


           Сила ^
        |
        |       / (отталкивание)
        |      /
        |     /
        |    / 
        |---/---> r = σ (сила = 0)
        |  / \
        | /   \
        |/     \ (притяжение)
   -----+---------→ Расстояние
        |       \
        |        \
        */
        F = 24 * EPS / r * (2 * pow(SIGMA_r, 12) - pow(SIGMA_r, 6));

}

// Вывод координат частиц
void print_r(std::ostream& os, unsigned int i, int DEFAULT_PRECISION) {
    os << "r" << i + 1 << " = ("
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << coordx[i] << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << coordy[i] << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << coordz[i] << ")\n";
}

// Вывод расстояния между частицами
void print_rij_abs(std::ostream& os, unsigned int i, unsigned int j, double r_ij_abs, int DEFAULT_PRECISION) {
    os << "r" << i + 1 << j + 1 << "_abs = "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << r_ij_abs << "\n";
}

// Вывод энергии и силы
void print_UF(std::ostream& os, unsigned int i, unsigned int j, int DEFAULT_PRECISION) {
    os << "U" << i + 1 << j + 1 << " = " << std::fixed << std::setprecision(DEFAULT_PRECISION) << U << "\n";
    os << "F" << i + 1 << j + 1 << " = " << std::fixed << std::setprecision(DEFAULT_PRECISION) << F << "\n";
}

// Вывод вектора расстояния между частицами
void print_rij(std::ostream& os, unsigned int i, unsigned int j, double rx_ij, double ry_ij, double rz_ij, int DEFAULT_PRECISION) {
    os << "r" << i + 1 << j + 1 << " = (rx" << i + 1 << j + 1 << "; ry" << i + 1 << j + 1 << "; rz" << i + 1 << j + 1 << ") = ("
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << rx_ij << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << ry_ij << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << rz_ij << ")\n";
}

// Вывод силы действующей на частицу
void print_next_F(std::ostream& os, unsigned int i, int DEFAULT_PRECISION) {
    os << "F" << i + 1 << " = (Fx" << i + 1 << "; Fy" << i + 1 << "; Fz" << i + 1 << ") = ("
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << Fx[i] << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << Fy[i] << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << Fz[i] << ")\n";
}

// Вывод скорости частицы
void print_v(std::ostream& os, unsigned int i, int DEFAULT_PRECISION) {
    os << "v" << i + 1 << " = (vx" << i + 1 << "; vy" << i + 1 << "; vz" << i + 1 << ") = ("
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << vx[i] << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << vy[i] << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << vz[i] << ")\n";
}

// Вывод единичного вектора направления
void print_rij_div(std::ostream& os, unsigned int i, unsigned int j, double rx_div, double ry_div, double rz_div, int DEFAULT_PRECISION) {
    os << "(rx" << i + 1 << j + 1 << "; ry" << i + 1 << j + 1 << "; rz" << i + 1 << j + 1 << ") / r" << i + 1 << j + 1 << "_abs = ("
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << rx_div << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << ry_div << "; "
        << std::fixed << std::setprecision(DEFAULT_PRECISION) << rz_div << ")\n";
}

// Изменение скорости в методе Верле
void veloсity_Verlet_0_5(unsigned int i) {
    /*
    Второй закон Ньютона a = F/m
    Для численного интегрирования используем приближение
    v(t + Δt/2) = v(t) + a(t) * (Δt/2)
    Fx[i] - сила по оси X для частицы i
    Fx[i] / MASS - ускорение по оси X (aₓ = Fₓ/m)
    Fx[i] / MASS * STEP - изменение скорости за полный шаг (Δv = a * Δt)
    Fx[i] / MASS * STEP / 2 - изменение скорости за половинный шаг (Δv = a * Δt/2)
    vx[i] += - обновление скорости
    */
    vx[i] += Fx[i] / 2 / MASS * STEP;
    vy[i] += Fy[i] / 2 / MASS * STEP;
    vz[i] += Fz[i] / 2 / MASS * STEP;
}
// Изменение координат в методе Верле
void coord_Verlet(unsigned int i) {
    coordx[i] += vx[i] * STEP;
    coordy[i] += vy[i] * STEP;
    coordz[i] += vz[i] * STEP;
}

// Расчёт силы действующую на частицу от другой частицы и 
// Расчет сил между частицами
// Расчет вириальной составляющей давления P2
void F_ij_and_P2(unsigned i, unsigned j, double rx_ij, double ry_ij, double rz_ij, double r_ab) {
    /*
    unsigned i, unsigned j: Индексы двух взаимодействующих частиц
    double rx_ij, ry_ij, rz_ij: Компоненты вектора расстояния между частицами
    double r_ab: Расстояние между частицами (модуль вектора расстояния).

    F * (rx_ij) / r_ab: Это проекция силы на ось X
    (rx_ij) / r_ab - это единичный вектор вдоль оси X, указывающий направление от частицы j к частице i. Это косинус угла между вектором расстояния и осью X
    x[i] += ...: Сила, действующая на частицу i, со стороны частицы j, добавляется к уже существующей силе на частице i (которая может включать вклады от других частиц)
    Fx[j] += F * (-rx_ij) / r_ab: Сила, действующая на частицу j. Вектор направления от i к j противоположен вектору от j к i, поэтому он берется с отрицательным знаком -rx_ij. Это гарантирует, что F_i = -F_j
    */
    Fx[i] += F * (rx_ij) / r_ab;
    Fy[i] += F * (ry_ij) / r_ab;
    Fz[i] += F * (rz_ij) / r_ab;
    Fx[j] += F * (-rx_ij) / r_ab;
    Fy[j] += F * (-ry_ij) / r_ab;
    Fz[j] += F * (-rz_ij) / r_ab;
    

    /*
    Вириал (Вириальная теорема): В статистической механике давление идеального газа (P = nkT) корректируется для реальных систем с взаимодействиями с помощью вириала.
    Вириал для парных сил определяется как сумма по всем парам: Σ (r_ij · F_i).
    r_ij - вектор расстояния.
    F_i - сила, действующая на частицу i со стороны частицы j.
    rx_ij * Fx[i] + ry_ij * Fy[i] + rz_ij * Fz[i] - это и есть скалярное произведение векторов r_ij и F_i, то есть вклад текущей пары в вириал.
    Формула давления: Давление системы вычисляется по формуле:
    P = (N * k * T) / V + (1 / (3 * V)) * Σ (r_ij · F_ij)
    где:
    N * k * T / V - вклад идеального газа (в вашем коде он, видимо, вычисляется отдельно).
    (1 / (3 * V)) * Σ (r_ij · F_ij) - вириальная поправка.
    1.0 / 3 / VOLUME * (...):
    VOLUME - объем системы (V).
    1/3 и 1/V - это как раз множитель 1/(3V) из формулы давления
    */
    P2 += 1.0 / 3 / VOLUME * (rx_ij * Fx[i] + ry_ij * Fy[i] + rz_ij * Fz[i]);

    
}
//ПГУ (переодические граничные условия)
void PBC(unsigned int i) {
    /*
    LX — длина по оси X
    LY — длина по оси Y
    LZ — длина по оси Z
    Координаты частицы с индексом i хранятся в массивах coordx[i], coordy[i], coordz[i]
    */
    if (coordx[i] >= LX) {
        coordx[i] -= LX;
    }
    if (coordx[i] < 0) {
        coordx[i] += LX;
    }
    if (coordy[i] >= LY) {
        coordy[i] -= LY;
    }
    if (coordy[i] < 0) {
        coordy[i] += LY;
    }
    if (coordz[i] >= LZ) {
        coordz[i] -= LZ;
    }
     if (coordz[i] < 0) {
        coordz[i] += LZ;
    }
}

// Скорость центра масс
void velocity_m(double& vx_m, double& vy_m, double& vz_m) {
    // Переменные vx_m, vy_m, vz_m, переданные по ссылке, обнуляются. Они будут накапливать сумму скоростей всех частиц
    vx_m = 0.0;
    vy_m = 0.0;
    vz_m = 0.0;

    // Суммирование скоростей
    for (unsigned int i = 0; i < NUMBERPARTICLES; i++) {
        vx_m += vx[i];
        vy_m += vy[i];
        vz_m += vz[i];
    }
    // Усреднение
    // После суммирования суммарные скорости делятся на общее количество частиц, чтобы получить среднее значение.
    vx_m /= NUMBERPARTICLES;
    vy_m /= NUMBERPARTICLES;
    vz_m /= NUMBERPARTICLES;
}

void macroparams() {
    double vx_m, vy_m, vz_m;

    // Получаем скорости центра масс
    /*
    Вызывается функция velocity_m, которая вычисляет среднюю скорость системы по каждой компоненте (скорость центра масс).
    Это нужно для разделения общего движения системы и теплового (хаотического) движения частиц.
    */
    velocity_m(vx_m, vy_m, vz_m);

    // Обнуляем энергии перед расчетом
    // Расчет энергий, температуры, давления
    Ekin = 0.0;
    Eterm = 0.0;

    // Вычисляем кинетическую и тепловую энергию
    for (unsigned int i = 0; i < NUMBERPARTICLES; i++) {
        // Полная кинетическая энергия
        /*
        Ekin — полная кинетическая энергия системы. Она вычисляется по стандартной формуле mv²/2 для каждой частицы и суммируется.
        */
        Ekin += MASS / 2 * (vx[i] * vx[i] + vy[i] * vy[i] + vz[i] * vz[i]);

        // Тепловая энергия 
        /*
        Eterm — тепловая (хаотическая) энергия.
        Она вычисляется как кинетическая энергия относительно движения центра масс (v[i] - v_m).
        Именно эта энергия связана с температурой системы.
        */
        Eterm += MASS / 2 * ((vx[i] - vx_m) * (vx[i] - vx_m) +
            (vy[i] - vy_m) * (vy[i] - vy_m) +
            (vz[i] - vz_m) * (vz[i] - vz_m));
    }
    /*
    P1 — "идеальная" составляющая давления.
    Рассчитывается по формуле, следующей из теоремы о равнораспределении и уравнения Клапейрона-Менделеева:
    P_ideal = (2/3) * (E_kinetic / V)
    Поскольку у нас Eterm — это именно кинетическая энергия хаотического движения, формула принимает вид P1 = (2 / VOLUME / 3) * Eterm
    */
    P1 = 2 / VOLUME / 3 * Eterm;
    /*
    P2 — "вириальная" составляющая давления.
    Предполагается, что она была вычислена ранее в ходе расчета сил
    */
    // P — полное давление в системе. Это сумма идеального и вириального вкладов: P = P_ideal + P_virial
    P = P1 + P2; // Полное давление
    /*
    T — температура системы. Вычисляется на основе тепловой энергии Eterm.
    Формула следует из теоремы о равнораспределении: на каждую степень свободы приходится энергия k_B * T / 2.
    У каждой частицы есть 3 степени свободы (движение по x, y, z). Поэтому суммарная тепловая энергия всех N частиц:
    Eterm = (3/2) * N * k_B * T
    Преобразуем эту формулу, чтобы найти температуру:
    T = (2/3) * (Eterm / N) / k_B
    */ 
    T = 2.0 / 3 * Eterm / NUMBERPARTICLES / K_B; // Температура

    /*
    E — полная энергия системы.
    Сумма полной кинетической (Ekin) и потенциальной (U) энергий.
    Это значение должно сохраняться (консервироваться) в неизолированной системе.
    */
    E = Ekin + U;
    /*
    Eint — внутренняя энергия. Сумма тепловой (хаотической) энергии (Eterm) и потенциальной энергии (U).
    Это ключевая термодинамическая величина.
    */
    Eint = Eterm + U;
    
}
void print_macroparams(std::ostream& os, int DEFAULT_PRECISION) {
    os << std::fixed << std::setprecision(DEFAULT_PRECISION);
    os << "Ekin = " << Ekin << "\n";
    os << "Eterm = " << Eterm << "\n";
    os << "Epot = " << U << "\n";  
    os << "Eint = " << Eint << "\n";
    os << "E = " << E << "\n";
    os << "T = " << T << "\n";
    os << "P = " << P << "\n";
/*    os << "P1 = " << P1 << "\n";   
    os << "P2 = " << P2 << "\n";  */ 
}

    

// ЛР 9
void MD_8() {
    double r_ab, rx_ij, ry_ij, rz_ij;
    using namespace std;
    //Задаём начальные условия
    start_cond_two_particles();
    std::ofstream outFile("Charykov.txt");

    outFile << fixed << setprecision(8);
    outFile << "Step = 0" << endl;
    for (unsigned int i = 0; i < NUMBERPARTICLES; i++) {
        print_r(outFile, i, 8);
        Fx[i] = 0; Fy[i] = 0; Fz[i] = 0;
    }

    //Нулевой шаг
    P2 = 0;

    // Нулевой шаг - расчет начальных сил
    // Основной цикл по шагам
    for (unsigned int i = 0; i < NUMBERPARTICLES; i++) {
        // Алгоритм Верле
        // Расчет сил
        // Расчет макропараметров
        // Вывод в файл

        for (unsigned int j = i + 1; j < NUMBERPARTICLES; j++) {
            rx_ij = coordx[i] - coordx[j];
            ry_ij = coordy[i] - coordy[j];
            rz_ij = coordz[i] - coordz[j];

            if (rx_ij > LX / 2) {
                rx_ij -= LX;
            }
            if (rx_ij < (-LX / 2)) {
                rx_ij += LX;
            }
            if (ry_ij > LY / 2) {
                ry_ij -= LY;
            }
            if (ry_ij < (-LY / 2)) {
                ry_ij += LY;
            }
            if (rz_ij > LZ / 2) {
                rz_ij -= LZ;
            }
            if (rz_ij < (-LZ / 2)) {
                rz_ij += LZ;
            }


            r_ab = r_abs(rx_ij, ry_ij, rz_ij);//Модуль радиус-вектора между i-ой и j-ой частицами
            if (r_ab <= RCUT) {
                calculate_U_F(r_ab);//Расчёт потенциальной энергии, сил по Л.-Дж.
                //Расчёт сил, действующих на частицы
                F_ij_and_P2(i, j, rx_ij, ry_ij, rz_ij, r_ab);
            
            }

            print_rij_abs(outFile, i, j, r_ab, 8);
            print_UF(outFile, i, j, 8);
            print_next_F(outFile, i, 8);
        }
        print_v(outFile, i, 8);
       
    }
    macroparams();
    print_macroparams(outFile, 8);
    //Шаги с первого по LASTSTEP
    for (unsigned int step = 1; step <= LASTSTEP; step++) {
        P2 = 0;
       
        outFile << "\nStep = " << step << endl;
        

        for (unsigned int i = 0; i < NUMBERPARTICLES; i++) {
            veloсity_Verlet_0_5(i);//Верле на временном шаге t+dt/2 : скорости 1/2
            
            coord_Verlet(i);//Верле на временном шаге t+dt : координаты
            PBC(i);

            
            print_r(outFile, i, 8);
            

            Fx[i] = 0.0; Fy[i] = 0.0; Fz[i] = 0.0;
        }
        for (unsigned int i = 0; i < NUMBERPARTICLES; i++) {
            for (unsigned int j = i + 1; j < NUMBERPARTICLES; j++) {
                rx_ij = coordx[i] - coordx[j];
                ry_ij = coordy[i] - coordy[j];
                rz_ij = coordz[i] - coordz[j];

                if (rx_ij > LX / 2) {
                    rx_ij -= LX;
                }
                if (rx_ij < (-LX / 2)) {
                    rx_ij += LX;
                }
                if (ry_ij > LY / 2) {
                    ry_ij -= LY;
                }
                if (ry_ij < (-LY / 2)) {
                    ry_ij += LY;
                }
                if (rz_ij > LZ / 2) {
                    rz_ij -= LZ;
                }
                if (rz_ij < (-LZ / 2)) {
                    rz_ij += LZ;
                }

                r_ab = r_abs(rx_ij, ry_ij, rz_ij); // Модуль радиус-вектора между i-ой и j-ой частицами
                if (r_ab <= RCUT) {
                    calculate_U_F(r_ab);//Расчёт потенциальной энергии, сил по Л.-Дж.
                    //Расчёт сил, действующих на частицы
                    F_ij_and_P2(i,j,rx_ij, ry_ij, rz_ij, r_ab);
                }
                else{
                    U = 0;
                    F = 0;
                }
                
                print_rij_abs(outFile, i, j, r_ab, 8);
                print_UF(outFile, i, j, 8);
                print_next_F(outFile, i, 8);
                
                
            }
            veloсity_Verlet_0_5(i);

            
            
             print_v(outFile, i, 8);
            
        }

        macroparams();
        print_macroparams(outFile, 8);
    }
        outFile << endl;
    
    outFile.close();
}



void memory_allocation() {
    // Выделение памяти под массивы
    const size_t size = NUMBERPARTICLES * sizeof(double);

    coordx = (double*)malloc(size);
    coordy = (double*)malloc(size);
    coordz = (double*)malloc(size);

    vx = (double*)malloc(size);
    vy = (double*)malloc(size);
    vz = (double*)malloc(size);

    Fx = (double*)malloc(size);
    Fy = (double*)malloc(size);
    Fz = (double*)malloc(size);
}

void memory_free() {
    // Освобождение памяти
    free(coordx);
    free(coordy);
    free(coordz);

    free(vx);
    free(vy);
    free(vz);

    free(Fx);
    free(Fy);
    free(Fz);
}


int main() {
    // Выделяем память 
    memory_allocation();
    // Запуск моделирования
    MD_8();
    
    //Освобождаем память 
    memory_free();

    return 0;
}
