#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Frank@Villaro-Dixon.eu - DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE, etc.

import requests
import json

class Elevation():
	api_version = 'v1'

	def __init__(self, base_url='http://elevationapi.xyz/api'):
		self.base_url = base_url

	def getElevation(self, point):
		'''Returns the elevation of a point. If point is a (lat, lon) tuple,
		then a scalar is returned. If point is a {'lat':…,'lon':…} dict, then
		a {'lat':…,'lon':…,'ele':…} dict is returned
		'''

		assert(type(point) == tuple)
		assert(len(point) == 2)
		base = 'point/{}/{}?format=short'.format(round(point[0], 3), round(point[1], 3))

		return self._get_json(base)

	def getElevations(self, points):
		'''Returns the elevation of a list of points. If the elements of the
		list are tuples, then a list of elevation (scalars) is returned. If
		the elements of the list are dicts ({'lat':…,'lon':…}), then a list
		of dicts is returned({'lat':…,'lon':…,'ele':…}).
		'''
		assert(type(points) == list)
		base = 'points'

		return self._get_json(base, {'points': json.dumps(points)})

	def _get_json(self, extension_url, data=None):
		url = self.base_url + '/' + self.api_version + '/' + extension_url

		r = requests.get(url, data=data)
		return r.json()



# vim: set ts=4 sw=4 noet:

