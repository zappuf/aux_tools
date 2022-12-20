#!/usr/bin/env python
import sys
from pathlib import Path
import glob
import logging
import argparse

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

NUCLEIC_ACID_EXTENSIONS = [".fa", ".fna", ".ffn", ".frn"]
ALL_SUFFIXES = NUCLEIC_ACID_EXTENSIONS + ['.gz', '.bgz']

def find_extension(input_file: Path):
    suffixes = input_file.suffixes
    logger.debug(f"Suffixes {suffixes}")
    mismatch_suffix = set(suffixes) - set(ALL_SUFFIXES)
    if len(mismatch_suffix) > 0: #check that all suffixes are allowed
        logging.info(f"Suffix {mismatch_suffix} not allowed.")
    else:
        matching_suffix = set(suffixes) & set(NUCLEIC_ACID_EXTENSIONS)
        if len(matching_suffix) == 1:
            logger.info(f"Matched fasta file {input_file}")
            return input_file
    return ""

def find_fasta_file(input_path: Path):
    input_files = glob.glob(str(input_path / "**/*.f*"), recursive=True)
    logger.debug(f"Found possible fasta matches: {input_files}")

    for input_file in input_files:
        input_file = Path(input_file)
        logger.debug(f"Input file {input_file}")
        fasta_file = find_extension(input_file)
        if fasta_file != "":
            return fasta_file

def main(argv=None):
    parser = argparse.ArgumentParser(description="Find fasta files recursively from input directory")
    parser.add_argument("--input_dir", help="Input path to search", default='../data', type=Path)

    if argv:
        args = parser.parse_args(argv)
    else:
        parser.print_usage()
        return 0
    input_dir = args.input_dir.absolute()
    logging.info(f"Input dir to search for fasta files {args.input_dir}")
    fasta_file = find_fasta_file(args.input_dir)
    if fasta_file:
        print(str(fasta_file))
    else:
        logger.error("Unable to find fasta file!")
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

def test_generic_fasta():
    input_file = Path("/data/test.fa")
    assert str(find_extension(input_file)) == "/data/test.fa"

def test_generic_gzip():
    input_file = Path("/data/test.fa.gz")
    assert str(find_extension(input_file)) == "/data/test.fa.gz"

def test_faindex():
    input_file = Path("/data/test.fa.gz.fai")
    assert str(find_extension(input_file)) == ""

def test_nucleic_acid_fasta():
    input_file = Path("/data/test.fna")
    assert str(find_extension(input_file)) == "/data/test.fna"