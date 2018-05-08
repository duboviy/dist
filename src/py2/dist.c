#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "dist.h"


// converts decimal degrees to radians
double _deg2rad(double deg) {
  return (deg * DEG_RAD);
}
 
// converts radians to decimal degrees
double _rad2deg(double rad) {
  return (rad * RAD_DEG);
}

// use Haversine Formula to calculate distance
double haversine(float lat1, float long1, float lat2, float long2)
{
    float theta = long1 - long2;
    float dist = sin(_deg2rad(lat1)) * sin(_deg2rad(lat2)) 
       + cos(_deg2rad(lat1)) * cos(_deg2rad(lat2)) * cos(_deg2rad(theta));

    dist = acos(dist);
    dist = _rad2deg(dist);
    dist = dist * MINUTE_IN_DEGREE * STATUTE_PER_MILLE * KM_IN_MILLE;
    
    return dist;
}

static PyObject* compute(PyObject* self, PyObject* args)
{
    float lat1;
    float long1;
    float lat2;
    float long2;

    if (!PyArg_ParseTuple(args, "ffff", &lat1, &long1, &lat2, &long2))
        return NULL;

    return Py_BuildValue("f", haversine(lat1, long1, lat2, long2));
}


static PyMethodDef DistanceMethods[] = {
    {"compute", compute, METH_VARARGS,
     "Calculate distance between two coordinates on the map."},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC
initdist(void)
{
    (void) Py_InitModule("dist", DistanceMethods);
}
