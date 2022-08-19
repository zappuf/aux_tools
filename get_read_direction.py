import sys

def get_read_direction(filepath):
    filename = filepath.split("/")[-1]
    return filename.split("_")[-1].split(".")[0]

print(get_read_direction(sys.argv[1]))
