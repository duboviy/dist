import math
import timeit

import dist


def pure_py_dist(lat1d, lon1d, lat2d, lon2d):
    """ Pure python implementation to compare performance with. """
    lat1 = math.radians(lat1d)
    lat2 = math.radians(lat2d)
    lon1 = math.radians(lon1d)
    lon2 = math.radians(lon2d)
    R = 3956  # miles
    d_miles = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)) * R * 1.609344
    return d_miles


def test_positive_scenario():
    lat1 = lng2 = lat2 = 10.1
    lng1 = 12.1

    assert int(dist.compute(lat1, lng1, lat2, lng2)) == int(pure_py_dist(lat1, lng1, lat2, lng2))


def compare_performance():
    pure_py_time = timeit.timeit("pure_py_dist(10.1, 12.1, 10.1, 10.1)", number=10000000,
                                 setup="from __main__ import pure_py_dist")
    ext_time = timeit.timeit("dist.compute(10.1, 12.1, 10.1, 10.1)", number=10000000,
                             setup="from __main__ import dist")
    print("ext_time: {} pure_py_time {}".format(pure_py_time, ext_time))
    # My Python/C API Extension is in ~ 3 times faster than fast pure python implementation
    assert ext_time < pure_py_time


if __name__ == '__main__':
    test_positive_scenario()
    compare_performance()


