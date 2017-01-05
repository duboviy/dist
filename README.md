dist
========

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c2828cf960c8404e86b487c0b79656ab)](https://www.codacy.com/app/dubovoy/dist?utm_source=github.com&utm_medium=referral&utm_content=duboviy/dist&utm_campaign=badger)

Python/C API extension module that computes distance between two coordinates on the world map.
You can get distance result in:
- miles (default)
- kilometers
- nautical miles


Why?
----

As more and more apps are using maps, the more demand for geolocation capabilities increase. As the name suggests, geolocation is about the reporting of your location to other users, as well as associating real-world locations (such as landmarks) to your location. This repo helps to accurately calculate the distance between two locations and presents a time efficient practical solution.


Installation
------------

    python setup.py install

Input data
----------
The distance function accepts five parameters:

- lat1, lon1: The Latitude and Longitude of point 1 (in decimal degrees)
- lat2, lon2: The Latitude and Longitude of point 2 (in decimal degrees)

- unit: The unit of measurement in which to calculate the results where:
    - 'M' is statute miles (default)
    - 'K' is kilometers
    - 'N' is nautical miles


Usage
-----

    >>> import distance
    >>> distance.compute(10.1, 12.1, 10.1, 10.1)
    136.039001465


Performance / speed comparison
------------------------------

This Python/C API Extension module is in ~ 3 times faster than similar fast pure python implementation.


Python Versions
---------------
Checked under Python 2.7 and Python 3.3


What does it use inside? What kind of formula implementation is used? 
---------------------------------------------------------------------

We should account for the curvature of the Earth when calculating large distances on world map. If the Earth were flat, calculating the distance between two points would be very simple as for a straight line. The Haversine formula is used in current implementation, it includes a constant that represents the radius of the Earth.
The Haversine formula is not 100% accurate because the Earth is not a perfect sphere. Though, the Haversine gives a good enough approximation for most applications that use geolocation.

_______________________________________
