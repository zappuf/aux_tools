#!/usr/bin/env python
import sys

def get_pattern_fwd(filename, direction="1"):
    direction_complement = "2" if direction == "1" else "1"
    pattern_list = filename.split("_")
    pattern = pattern_list[-1]
    return pattern if direction in pattern else pattern.replace(direction_complement, direction)

print(get_pattern_fwd(sys.argv[1], sys.argv[2]))
