from setuptools import setup

setup(name="syncnames",
	  version="1.0",
	  description="Sunchronizes the name of file and folder (along with contents in folder) to a single given name",
	  author="Shivaji Byrapaneni",
	  py_module=['syncnames'],
	  install_rqeuires=[
	  		'Click',
	  ],
	  entry_points='''
	  		[console_scripts]
	  		syncnames=syncnames:sync
	  ''',
	)