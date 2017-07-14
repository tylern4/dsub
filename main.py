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
from batch import batch, make_list


def main():
    # Make argument parser
    parser = argparse.ArgumentParser(description="A PBS system for docker")
    parser.add_argument('-c', dest='cores', type=int, nargs='?', help="Number of cores to use if not all the cores", default=0)
    parser.add_argument('-n', dest='num', type=int, nargs='?', help="Number of simulations to do", default=10)
    parser.add_argument('-o', dest='output', type=str, nargs='?', help="Output directory for final root files", default=".")
    parser.add_argument('-p', dest='prog', help="Use Progress Bar", action='store_true')
    parser.set_defaults(prog=False)

    args = parser.parse_args()

    # Make sure file paths have ending /
    if args.output[-1] != '/':
        args.output = args.output + '/'
    if args.cores == 0 or cpu_count > cpu_count():
        args.cores = cpu_count()

    files = make_list(args)
    pool = Pool(processes=args.cores)

    if has_prog and args.prog:
        for _ in tqdm.tqdm(pool.imap_unordered(batch, files), total=args.num):
            pass
    else:
        pool.map(batch, files)

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
