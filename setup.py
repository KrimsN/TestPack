from setuptools import setup, find_packages

setup(name='TestPack',
      version='0.0.3',
      description='My test python package',
      author='KrimsN',
      author_email='dr.krimsn@gmail.com',
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
     )