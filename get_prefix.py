import sys

def get_prefix(filename):
    prefix_list = filename.split("_")[:-1]
    return "_".join(prefix_list)

print(get_prefix(sys.argv[1]))
