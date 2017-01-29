<h1><img src="https://raw.githubusercontent.com/duboviy/dist/master/logo.png" height=85 alt="logo" title="logo"> dist</h1>

by [Eugene Duboviy](https://duboviy.github.io/)

[![Build Status](https://travis-ci.org/duboviy/dist.svg?branch=master)](https://travis-ci.org/duboviy/dist) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/c2828cf960c8404e86b487c0b79656ab)](https://www.codacy.com/app/dubovoy/dist?utm_source=github.com&utm_medium=referral&utm_content=duboviy/dist&utm_campaign=badger) [![Code Health](https://landscape.io/github/duboviy/dist/master/landscape.svg?style=flat)](https://landscape.io/github/duboviy/dist/master) [![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/duboviy/dist/) [![PRs & Issues Welcome](https://img.shields.io/badge/PRs%20&%20Issues-welcome-brightgreen.svg)](https://github.com/duboviy/dist/pulls) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/duboviy/dist/) 

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

This Python/C API Extension module is **in ~ 3 times faster than similar fast pure python implementation**. You can use performance test to compare speed with fast pure python implementation, just run nose test runner:

```
>>> nosetests
ext_time: 2.46785402298 pure_py_time: 7.49713611603
```


Python Versions
---------------
Checked under following Python versions:
* "2.5"
* "2.6"
* "2.7"
* "3.3"
* "3.4"
* "3.5"
* "3.6"


What does it use inside? What kind of formula implementation is used? 
---------------------------------------------------------------------

Module accounts the curvature of the Earth when calculating large distances on the world map. If the Earth were flat, calculating the distance between two points would be very simple as for a straight line. The Haversine formula is used in current implementation, it includes a constant that represents the radius of the Earth.
The Haversine formula is not 100% accurate because the Earth is not a perfect sphere. However, the Haversine gives a good enough approximation for most applications that use geolocation.


License
---------------------------------------------------------------------

**MIT** licensed library. See [LICENSE.txt](LICENSE.txt) for details.


Contributing
---------------------------------------------------------------------

If you have suggestions for improving the dist, please [open an issue or
pull request on GitHub](https://github.com/duboviy/dist/).


Badges
---------------------------------------------------------------------

[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/duboviy/dist/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/duboviy/dist/) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](https://github.com/duboviy/dist/) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](https://github.com/duboviy/dist/)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/duboviy/dist/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://github.com/duboviy/dist/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](https://github.com/duboviy/dist/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://github.com/duboviy/dist/)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/duboviy/dist/)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/duboviy/dist/)

_______________________________________
