"""PyBuster

Usage:
   pybuster.py [-w <wordlist>] [-o <out>] <url>
   pybuster.py (-h | --help)
   pybuster.py --version

Options:
   -w <wordlist>   Name of file containing directory names to use.
   -o <out>        File name to write output to.
   -h --help       Show this screen.
   --version       Show version.
"""
from external.docopt import docopt


__version__ = "0.0.1"


def main(url, wordlist=None, out=None):
    """Takes server URL, scans for directories, and writes responses to file.

    If wordlist is specified makes requests for directories listed in wordlist,
    otherwise uses a default list of common directory names. It is recommended
    that an output file name is specified; if none is given, writes to
    pybuster_out.txt.

    Args:
        url: The URL of the server to scan.
        wordlist: Path for text file containing one directory name per line.
        out: File name to write output to.

    Returns:
        None
    """
    pass


if __name__ == "__main__":
    PKG_VER = "PyBuster " + __version__
    ARGS = docopt(__doc__, version=PKG_VER)

    #check input for option flags and get corresponding arguments
    if ARGS["-w"] is not None:
        WORDLIST = ARGS["<wordlist>"]
    else:
        WORDLIST = None

    if ARGS["-o"] is not None:
        OUT = ARGS["<out>"]
    else:
        OUT = None

    main(ARGS["<url>"], wordlist=WORDLIST, out=OUT)
