#!/usr/bin/env python
import sys

def get_prefix(filename="", split_position="-1"):
    if "_" in filename:
        prefix_list = filename.split("_")[:int(split_position)]
        return "_".join(prefix_list)
    else:
        return filename.split(".")[0]
print(get_prefix(sys.argv[1], sys.argv[2]))
