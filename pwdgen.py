#! /usr/bin/python3

import argparse
from collections import namedtuple
import csv
from math import log2
import secrets

parser = argparse.ArgumentParser(
    "pwdgen",
    description="Generate password with selected entropy"
)

parser.add_argument('--dictionary', type=argparse.FileType())

args = parser.parse_args()

WordRecord = namedtuple("WordRecord", ['word', 'entropy'])

with args.dictionary as f:
    rows = csv.reader(f)
    wordrecords = [WordRecord(w, float(e)) for w, e in rows]

prepass = [ secrets.choice(wordrecords) for _ in range(4) ]


print( ' '.join([word for word, _ in prepass]) )
print('Words:', len(prepass))
print('Linguistic entropy (approx.):', sum(e for _, e in prepass), 'bits')
print('Known-dictionary entropy:', log2(len(wordrecords))*len(prepass), 'bits')
