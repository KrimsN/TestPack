from distutils.core import setup

setup(name='TestPack',
      version='0.0.1',
      description='My test python package',
      author='KrimsN',
      author_email='dr.krimsn@gmail.com',
      packages=['test_pack', 'test_pack.test_module'],
     )