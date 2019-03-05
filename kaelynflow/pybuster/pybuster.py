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
from external.docopt import docopt


__version__ = "0.0.1"


def manager(url, dir_file=None):
    """Takes server URL, scans for directories, and writes responses to file.
    
    If dir_file is specified makes requests for directories listed in dir_file, 
    otherwise performs a brute force scan.
    
    Args:
        url: The URL of the server to scan.
        dir_file: Path for text file containing one directory name per line.
    
    Returns:
        None
    """
    pass


if __name__ == "__main__":
    arguments = docopt(__doc__, version="PyBuster 0.0.1")

    if arguments["-d"] is not None:
        manager(arguments["<url>"], dir_file=arguments["<file>"])
    else:
        manager(arguments["<url>"])
