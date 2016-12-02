#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Frank@Villaro-Dixon.eu - DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE, etc.

import time
from Elevation import Elevation


e = Elevation()

print(e.getElevation((46.6, 6)))

point = {
	'lat': 46.6,
	'lon': 6
}
print(e.getElevation(point))

pts = [(46.1, 6.1), (47.2, 6.1), (46.46, 6.47)]
print(e.getElevations(pts))


##5.21
t = time.time()
pts = [(46.1, 6.1)] * 1000
e.getElevations(pts)
print(time.time() - t)

t = time.time()
pts = [{'lat':46.1, 'lon':6.1}] * 1000
e.getElevations(pts)
print(time.time() - t)

# vim: set ts=4 sw=4 noet:

