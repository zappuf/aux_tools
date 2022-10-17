#!/usr/bin/env python
import sys

def get_prefix(filename="", split_position="-1"):
    if "_" in filename and int(split_position):
        prefix_list = filename.split("_")[:int(split_position)]
        return "_".join(prefix_list)
    else:
        return filename.split(".")[0]

if len(sys.argv) > 2:
    print(get_prefix(sys.argv[1], sys.argv[2]))
else:
    print(get_prefix(sys.argv[1]))
