import sys

from distutils.core import setup, Extension


if sys.version_info[0] == 3:    # "using Python 3"
    ext = Extension("distance", sources=["src/py3/dist.c"])
elif sys.version_info[0] == 2:  # "using Python 2"
    ext = Extension("distance", sources=["src/py2/dist.c"])
else:
    raise NotImplementedError("Your python version is the biggest mystery I've ever seen yet!")

setup(
    name="dist",
    version="0.0.1",
    description="Compute distance between two coordinates on the map",
    ext_modules=[ext],
)
