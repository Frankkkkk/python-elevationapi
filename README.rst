python-elevationapi — Get the elevation of (almost) any point on Earth
======================================================================

elevationapi is a simple library that interfaces with
http://www.elevationapi.xyz . It permits you to get the elevation of
almost any point on Earth.

Example
-------

.. code:: python

    from elevationapi import Elevation
    e = Elevation()

    elevation_of_Geneva = e.getElevation(46.2, 6.15)

    #When asking for multiple points, use this instead:
    elevations = e.getElevations((46.2, 6.15), (6.3, 6.20))

Using another API provider
--------------------------

Simply instance Elevation with:

.. code:: python

    e = Elevation(base_url='http://your-server.tld/api')


