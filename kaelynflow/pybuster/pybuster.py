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
import os.path
import time
import requests
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
    #TODO(kaelynflow): Thorough checking/sanitization
    if url[-1] != "/":
        url += "/"

    if wordlist is None:
        wordlist = "resources/wordlist_medium.txt"

    if out is None:
        out = "pybuster_out.txt"

    #TODO(kaelynflow): Implement quiet error handling and logging
    if not os.path.exists(wordlist):
        err_msg = "No such file or directory: '{0}'".format(wordlist)
        raise FileNotFoundError(err_msg)

    response_dict = {} # holds url/response code pairs

    with open(wordlist, "r") as infile:
        #TODO(kaelynflow): Implement quiet error handling and logging
        for dir_name in infile:
            dir_url = url + dir_name.strip() + "/"
            response = requests.get(dir_url)

            start_time = time.time()
            # If rate-limited, try waiting 10ms intervals
            while response.status_code == 429 and time.time() - start_time < 1:
                time.sleep(0.01)
                response = requests.get(dir_url)

            response_dict[response.url] = response.status_code


    with open(out, "w") as outfile:
        for dir_url in response_dict:
            line = dir_url + " " + str(response_dict[dir_url]) + "\n"
            outfile.write(line)


if __name__ == "__main__":
    PKG_VER = "PyBuster " + __version__
    args = docopt(__doc__, version=PKG_VER)

    main(args["<url>"], wordlist=args["-w"], out=args["-o"])
