from distutils.core import setup

long_description = open('README.rst').read()

setup(
	name = 'elevationapi',
	packages = ['elevationapi'],
	version = '1.0.0',
	description = 'Get the elevation of any land point on Earth using elevationapi.xyz',
	long_description=long_description,
	author = 'Frank Villaro-Dixon',
	author_email = 'frank@villaro-dixon.eu',
	url = 'https://github.com/Frankkkkk/python-elevationapi',
#	download_url = 'https://github.com/Frankkkkk/python-elevationapi/tarball/0.1',
	keywords = 'elevation altitude earth elevationapi.xyz',
	classifiers = [
		'Topic :: Scientific/Engineering :: Atmospheric Science',
		'Topic :: Scientific/Engineering :: GIS',

		'License :: OSI Approved :: MIT License',

		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5'
		],
)
