# PyBuster

PyBuster is a python implementation of a CLI web server directory enumerator, with features modeled on dirBuster. Current version is non-functional skeleton. Currently tested on python 3.7 with plans for general python 3.x support.

## Virtual Environment Setup

To create an anaconda environment on macOS exactly duplicating the development environment of PyBuster, use
```shell
conda create --name <env> --file requirements.txt
```
For other systems, instead use
```shell
conda env create --name <env> --file requirements.yml
```