#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("outfile",help="Output file")
args = parser.parse_args()

C = list(range(0x1A20, 0x1A4D))
V = list(range(0x1A62, 0x1A74))

with open(args.outfile, "w", encoding="utf-8") as outf:
    res = [" ".join("{}{}".format(chr(c), chr(v)) for v in V) for c in C]
    outf.write("\n".join(res))
