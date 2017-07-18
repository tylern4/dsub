#!/usr/bin/env python
from __future__ import print_function

## Not Optional/builtin
from multiprocessing import Pool, cpu_count
import multiprocessing as mp
import argparse
import glob
import os

## My libraries
from logs import *
from temp_dir import cd, tempdir
from batch import batch
from xml_parse import xml_parse

def main():
    # Make argument parser
    parser = argparse.ArgumentParser(description="A PBS system for docker")
    parser.add_argument('-x', dest='xml_file', type=str, nargs='?', help="xml_file", default="test.xml")
    parser.add_argument('-p', dest='prog', help="Use Progress Bar", action='store_true')
    parser.set_defaults(prog=False)

    args = parser.parse_args()

    xml_data = xml_parse(args.xml_file)

    pool = Pool(processes=xml_data[0]['num_cores'])

    if has_prog and args.prog:
        for _ in tqdm.tqdm(pool.imap_unordered(batch, xml_data), total=xml_data[0]['count']):
            pass
    else:
        pool.map_async(batch, xml_data)

    # Close and join pool
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
    ####try:
    ####    main()
    ####except KeyboardInterrupt:
    ####    print_red("\n\nExiting")
    ####    sys.exit()
