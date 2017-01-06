dist
========

Python/C API extension module that computes distance between two coordinates on the world map.


Why?
----

As more and more apps are using maps, the more demand for geolocation capabilities increase.  Geolocation is about the reporting of your location to other users, as well as associating real-world locations (such as landmarks) to your location. This repo helps to accurately calculate the distance between two locations and presents a time efficient practical solution, that is almost 3 times faster than similar fast pure python implementation.


Installation
------------

    python setup.py install


Input and output data
----------
The dist function accepts four float parameters:

- lat1, lon1: The Latitude and Longitude of point 1 (in decimal degrees)
- lat2, lon2: The Latitude and Longitude of point 2 (in decimal degrees)

The unit of measurement in which result is calculated is kilometers. [float]


Usage
-----

    >>> import dist
    >>> dist.compute(10.1, 12.1, 10.1, 10.1)
    218.933532715


Performance / speed comparison
------------------------------

This Python/C API Extension module is **in ~ 3 times faster than similar fast pure python implementation**. You can use following script to compare performance / speed with fast pure python implementation:

```
>>> python compare_performance.py
ext_time: 7.49713611603 pure_py_time 2.46785402298
```


Python Versions
---------------
Checked under Python 2.7 and Python 3.3


What does it use inside? What kind of formula implementation is used? 
---------------------------------------------------------------------

Module accounts the curvature of the Earth when calculating large distances on the world map. If the Earth were flat, calculating the distance between two points would be very simple as for a straight line. The Haversine formula is used in current implementation, it includes a constant that represents the radius of the Earth.
The Haversine formula is not 100% accurate because the Earth is not a perfect sphere. However, the Haversine gives a good enough approximation for most applications that use geolocation.

_______________________________________
