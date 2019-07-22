[![CircleCI](https://circleci.com/gh/aliartiza75/python-list-comparison.svg?style=svg)](https://circleci.com/gh/aliartiza75/python-list-comparison)

# pylistcompare

A module to compare two lists that complex data in it.


# Installation guidelines

* Install the module
```bash
$ pip3 install listcompare
```
OR

```bash
$ pip install listcompare
```

## Usage guidelines

Import the module in your file or ipython3 shell

```bash
$ import listcompare

$ lis1 = [1, 2, 3]
$ lis2 = [2, 1, 3]

$ listcompare.compare_list(lis1, lis2)
$[output] True


$ lis1 = [1, 2, "3"]
$ lis2 = [2, 1, 3]

$ listcompare.compare_list(lis1, lis2)
$[output] False

``` 

## Project dependencies installation guidelines

Run this command to install the dependencies
```bash
$ sudo pip3 install -r requirements.txt
```

## Project distribution pusblishing guidelines

* Update the setup.py file in the root directory.
* To create source distribution run the command given below:
```bash
$ python3 setup.py sdist
```
* I will use [twine](https://pypi.org/project/twine/) to publish my package distribution
```bash
$ pip3 install twine
$ sudo twine upload dist/* # it will ask for username and password
```
Sometime twine can publish the distribution because of authentication issue but mostly works on 2nd or 3rd retry.

## Guidelines for cythonizing the project
```bash
$ cd listcompare
$ python setup.py build_ext --inplace 
```

## Project distribution page of pypi

Link to the pypi module [page](https://pypi.org/project/listcompare/)
Link to module webpage [page](https://aliartiza75.github.io/python-list-comparison/)
