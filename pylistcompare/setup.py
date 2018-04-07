from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'List comparision code',
  ext_modules = cythonize("pylistcompare.pyx"),
)
