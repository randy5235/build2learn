"""PyBuster

Usage:
   pybuster.py [-d <file>] <url>
   pybuster.py (-h | --help)
   pybuster.py --version

Options:
   -d <file>   Use directory names from file.
   -h --help   Show this screen.
   --version   Show version.
"""
from docopt import docopt


__version__ = "0.0.1"


def handler(url, dir_file=None):
    pass


if __name__ == "__main__":
    arguments = docopt(__doc__, version="PyBuster 0.0.1")

    handler(arguments["URL"], dir_file=arguments["-d"])
