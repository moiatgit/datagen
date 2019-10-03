#! /usr/bin/env python3
"""
    This script takes one or more filenames from commandline and
    stdoutputs the lines in these files so:
    - each line is unique
    - lines are alphanumerically sorted
    - whitespaces are trimmed
"""

import sys
import os


def process_file(contents, path):
    """ given a path to an existing file, it loads its contents and keeps them
        in the set of lines """
    with open(path) as f:
        lines = f.readlines()
        lines = [ l.strip() for l in lines ]
        lines = [ l for l in lines if len(l) ]
        contents.update(lines)


def process_files(contents, paths):
    """ processes a list of one or more paths """
    for p in paths:
        process_file(contents, p)


def show_results(contents):
    """ shows the contents sorted """
    for line in sorted(contents):
        print(line)


def main(argv):
    """ From the commandline arguments, this method gets the arguments
        checks them and performs the script task
    """
    if len(argv) == 1:
        print("Merges one or more files' contents")
        print("Usage: %s path2file1 path2file2…" % argv[0])
        sys.exit(1)

    for a in argv[1:]:
        if not os.path.isfile(a):
            print("ERROR: file %s not found" % a)
            sys.exit(1)

    contents = set()
    process_files(contents, argv[1:])
    show_results(contents)


if __name__ == '__main__':
    main(sys.argv)
