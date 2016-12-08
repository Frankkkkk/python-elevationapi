# elevationapi — Get the elevation of (almost) any point on earth
python-elevationapi is a simple library that interfaces with 
http://www.elevationapi.xyz .


## How to use
Usage is very simple. First import the module:

`from elevationapi import ElevationAPI`

then, create an Elevationapi object:

`e = ElevationAPI()`

Now, when you want to know the elevation of a point, simply use:

`elevation_of_Geneva = e.getElevation(46.2, 6.15)`

When you want to know the elevation of a *list of points*, use instead:

`elevations = e.getElevations((46.2, 6.15), (6.3, 6.20))`
