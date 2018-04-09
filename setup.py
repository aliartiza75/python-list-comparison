from setuptools import setup

setup(name='listcompare',
      version='1.1.10',
      url='https://github.com/aliartiza75/python-list-comparison.git',
      author='Irtiza Ali',
      description="This module provides support to compare two lists that have same or different types of data in it.",
      long_description="This module provides support to compare two lists that have same or different types of data in it."+
                       "\n Examples \n"+
                             "lis1 = [1,2,3] \n"+
                             "lis2 = [2,1] \n"+
                             "plc.compare_list(lis1, dlis2) # Frue \n"+

                             "lis1 = [1,2,3] \n"+
                             "lis2 = [2,1,'3'] \n"+
                             "plc.compare_list(lis1, lis2) # False \n"+

                             "lis1 = ['1','2','3'] \n"+
                             "lis2 = ['2','1'] \n"+
                             "plc.compare_list(lis1, lis2) # False \n"+

                             "lis1 = [1,2,3] \n"+
                             "lis2 = [2,1,3] \n"+
                             "plc.compare_list(lis1, lis2) # True \n"+

                             "lis1 = [{1:1,2:2}] \n"+
                             "lis2 = [{1:1,2:2}] \n"+
                             "plc.compare_list(lis1, lis2) # True \n"
                                 
                             "lis1 = 123 \n"+
                             "lis2 = [{1:1,2:2}] \n"+
                             "plc.compare_list(lis1, lis2) # Exception will be raised \n"

      ,
      author_email='aliartiza75@yahoo.com',
      license='GNU GENERAL PUBLIC LICENSE',
      classifiers=[  
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
      ],
      keywords='list comparision python3 python2 python listofdifferentdatatypes',
      packages=['listcompare'],
      zip_safe=False)
