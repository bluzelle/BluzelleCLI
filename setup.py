try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup


setup(name='BluzellePyConsole',
      version='1.0.0',
      description='Python implementation for Bluzelle Console',
      url='http://github.com/bluzelle/BluzellePyConsole',
      author='matteyu',
      author_email='matthew@bluzelle.com',
      license='Apache2.0',
      packages=['utils'],
      install_requires=['PyInquirer',
                        'factory_boy',
                        'pyfiglet',
                        'termcolor',
                        'regex'],
      zip_safe=False)
