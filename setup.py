import sys

from distutils.core import setup, Extension


if sys.version_info[0] == 3:    # "using Python 3"
    ext = Extension("dist", sources=["src/py3/dist.c"])
elif sys.version_info[0] == 2:  # "using Python 2"
    ext = Extension("dist", sources=["src/py2/dist.c"])
else:
    raise NotImplementedError("Not implemented for your python version")

setup(
    name="dist",
    version="1.0.3",
    description="Compute distance between two coordinates on the map",
    author='Eugene Duboviy',
    author_email='eugene.dubovoy@gmail.com',
    url='https://github.com/duboviy/dist',
    download_url = 'https://github.com/duboviy/dist/tarball/1.0.3',
    keywords = ['distance', 'coordinates', 'map', 'performance'],
    classifiers=[
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description="""
As more and more apps are using maps, the more demand for geolocation capabilities increase.
Geolocation is about the reporting of your location to other users,
as well as associating real-world locations (such as landmarks) to your location.
This repo helps to accurately calculate the distance between two locations
and presents a time efficient practical solution,
that is almost 3 times faster than similar fast pure python implementation.
""",
    ext_modules=[ext],
)
