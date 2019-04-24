from setuptools import setup

setup(name='btfxwss2', version='1.2.1', author='Nils Diefenbach',
      author_email='23okrs20+pypi@mykolab.com',
      url="https://github.com/xmurobi/btfxwss", license='LICENCSE',
      packages=['btfxwss'], install_requires=['websocket-client'],
      description="Python 3.5+ Websocket Client for the Bitfinex WSS API.")
