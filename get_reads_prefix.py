#!/usr/bin/env python
import sys

def get_reads_prefix(filename):
    prefix_list = filename.split("_")[:-1]
    return "_".join(prefix_list)

print(get_reads_prefix(sys.argv[1]))
