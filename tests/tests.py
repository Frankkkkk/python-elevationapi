#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Frank@Villaro-Dixon.eu - DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE, etc.

import unittest, sys
import random
from elevationapi import Elevation

class CustomAssertions: #{{{
	def assertElevsNear(self, ret, eles):
		if type(ret) == list:
			for i in range(len(ret)):
				r = ret[i]
				self.assertElevsNear(r, eles[i])
		else:
			if type(ret) == dict:
				self.assertElevsNear(ret['ele'], ele)

			if abs((ret-eles)/ret) > 0.05:
					raise AssertionError('{} is too far away from {}'.format(e1, e2))

#}}}


#localhost = 'http://localhost:5000/api'
localhost = 'http://elevationapi.xyz/api'

class TestElevation(unittest.TestCase, CustomAssertions):

	def testPointShort(self):
		e = Elevation(base_url=localhost)
		pt = (46.41, 6.84) #inside Lake Geneva@372m

		#given a tuple, expect a scalar
		self.assertEqual(type(e.getElevation(pt)), int)

		#Correct value
		self.assertElevsNear(e.getElevation(pt), 375)


	def testListTuple(self):
		e = Elevation(base_url=localhost)
		pts = [(46.1, 6.1), (47.2, 6.1), (46.46, 6.47)]
		eles = [643, 414, 370]
		rets = e.getElevations(pts)

		#Returns a list
		self.assertEqual(type(rets), list)

		for r in rets:
			#Given tuples, expect scalar
			self.assertEqual(type(r), int)

		#Of good values
		self.assertElevsNear(rets, eles)



if __name__ == '__main__':
	unittest.main()



# vim: set ts=4 sw=4 noet:

