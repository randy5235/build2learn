"""PyBuster

Usage:
   pybuster.py [-w <wordlist>] [-o <out>] <url>
   pybuster.py (-h | --help)
   pybuster.py --version

Options:
   -w <wordlist>   Name of file containing directory names to use.
   -o <out>     File name to write output to.
   -h --help       Show this screen.
   --version       Show version.
"""
from external.docopt import docopt


__version__ = "0.0.1"


def manager(url, wordlist=None, outfile=None):
    """Takes server URL, scans for directories, and writes responses to file.

    If dir_file is specified makes requests for directories listed in dir_file,
    otherwise performs a brute force scan.

    Args:
        url: The URL of the server to scan.
        wordlist: Path for text file containing one directory name per line.
        outfile: File name to write output to.

    Returns:
        None
    """
    pass


if __name__ == "__main__":
    arguments = docopt(__doc__, version="PyBuster "+__version__)

    #check input for option flags and get associated arguments
    if arguments["-w"] is not None:
        wfile = arguments["<wordlist>"]
    else:
        wfile = None

    if arguments["-o"] is not None:
        out = arguments["<out>"]
    else:
        out = None

    manager(arguments["<url>"], wordlist=wfile, outfile=out)
