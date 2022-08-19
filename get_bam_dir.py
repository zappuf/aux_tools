import sys

def get_bam_dir(path):
    path_list = path.split("/")[0:-1]
    return "/".join(path_list)

print(get_bam_dir(sys.argv[1]))
