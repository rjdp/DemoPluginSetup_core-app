from setuptools import setup

setup(name='abc',
      version='0.1',
      description='test',
      url='http://github.com/rjdp',
      author='rajdeep',
      author_email='rajdeep.sharma@rtcamp.com',
      license='MIT',
      packages=['cli'],
      install_requires=[
          'cement',
      ],
      entry_points = {
        'console_scripts': ['testmain=cli.abc:main'],
      },
      zip_safe=False)