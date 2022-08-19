#!/usr/bin/env python
import sys

def get_tg_prefix(filepath):
    filename = filepath.split("/")[-1]
    prefix_list = filename.split("_")[:-2]
    return "_".join(prefix_list)

print(get_tg_prefix(sys.argv[1]))
