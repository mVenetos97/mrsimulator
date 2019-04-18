
#include "leboct31.h"

OCPowderScheme leboct31(void)
{
    double *weights = createDouble1DArray(31);
    double pi = 3.14159265358979323846;
    double deg_to_rad = pi/180.;
    double alpha[31] = {
        0.00000000,
        0.00000000,
        0.00000000,
        0.00000000,
        0.00000000,
        7.52995108,
        10.7708560,
        16.8498911,
        17.5875412,
        20.2288199,
        25.0816830,
        29.7677350,
        32.1331436,
        45.0000000,
        45.0000000,
        45.0000000,
        45.0000000,
        45.0000000,
        45.0000000,
        57.8668563,
        60.2322650,
        64.9183170,
        69.7711801,
        72.4124588,
        73.1501089,
        79.2291440,
        82.4700489,
        90.0000000,
        90.0000000,
        90.0000000,
        90.0000000
    };
    double beta[31] = {
        0.0000000,
        20.2288199,
        45.0000000,
        69.7711801,
        90.0000000,
        82.5342479,
        58.3237741,
        33.2761302,
        73.1871458,
        90.0000000,
        47.8327264,
        63.5962810,
        80.8487219,
        10.5884838,
        24.1455738,
        38.9683735,
        54.7356103,
        71.6876561,
        90.0000000,
        80.8487219,
        63.5962810,
        47.8327264,
        90.0000000,
        73.1871458,
        33.2761302,
        58.3237741,
        82.5342479,
        20.2288199,
        45.0000000,
        69.7711801,
        90.0000000
    };

    double weight[31] = {
        0.003564681,
        0.020207384,
        0.022867624,
        0.020207384,
        0.003564681,
        0.032854216,
        0.044241991,
        0.044241991,
        0.041265902,
        0.020207384,
        0.044869633,
        0.044150172,
        0.044241991,
        0.032854216,
        0.041265902,
        0.044150172,
        0.044587065,
        0.044869633,
        0.022867624,
        0.044241991,
        0.044150172,
        0.044869633,
        0.020207384,
        0.041265902,
        0.044241991,
        0.044241991,
        0.032854216,
        0.020207384,
        0.022867624,
        0.020207384,
        0.003564681
    };
    OCEulerAngle *powderAngles = malloc(sizeof(OCEulerAngle)*31);
    for(int i=0; i<31; i++){
            OCEulerAngle angle = {alpha[i]*deg_to_rad, beta[i]*deg_to_rad, 0.0};
            powderAngles[i] = angle;
            weights[i] = weight[i];
        }
    OCPowderScheme powder_scheme = {
            powderAngles,
            weights,
            31
    };
    return powder_scheme;
}

