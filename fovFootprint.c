/*Sample function that will take altitude, angle data, and Pi Cam v2 specs, and output the Nadir FOV.
Function is a WIP.
The math used to develop this function was taken from the following stackexchange thread:
https://photo.stackexchange.com/questions/56596/how-do-i-calculate-the-ground-footprint-of-an-aerial-camera
The earth's curvature is not taken into account for these calculations.*/

//For reference: Pi Cam v2's xFOV angle is 62.2, yFOV is 48.8 in degrees

#include <stdio.h>
#include <math.h>

double calcFOV(double alti, double xsensor, double ysensor, double xgimbal, double ygimbal);    //function prototype{
double toRad(double degreeVal);

int main() {
    double alti = 100;   //altitude: we will later change this value to accept the sensor team's alti data
    double xsensor = 39.6;  //these are the horizontal and vertical FOV angles of the sensor in degrees, constants based on camera specs
    double ysensor = 26.99;
    double xgimbal = 30;        //these are the horizontal and vertical gimbal angles, should be based on servo angles
    double ygimbal = 30;

    calcFOV(alti, xsensor, ysensor, xgimbal, ygimbal);

    return 0;
}

double toRad(double degreeVal) {
    return degreeVal*(M_PI / 180);
}

double calcFOV(double alti, double xsensor, double ysensor, double xgimbal, double ygimbal) {
    
    double distBot, distTop, distLeft, distRight;  //the distances between the camera and the top, bottom, left and right sides of the footprint image
    double xfootprint, yfootprint;  //these are the horizontal and vertical dimensions of the ground footprint in meters

    distBot = alti*tan(toRad(ygimbal-(0.5*xsensor)));      //not sure if the gimbal angle variables should be reversed
    distTop = alti*tan(toRad(ygimbal+(0.5*xsensor)));
    distLeft = alti*tan(toRad(xgimbal-(0.5*ysensor)));
    distRight = alti*tan(toRad(xgimbal+(0.5*ysensor)));

    xfootprint = fabs(distTop-distBot);       //These measurements must be the absolute value of the difference, since we don't know which distance is greaterm
    yfootprint = fabs(distLeft-distRight);
   
    printf("The width of the camera FOV footprint is %.2f\n", xfootprint);
    printf("The height of the camera FOV footprint is %.2f\n", yfootprint);

    return 0;
}


