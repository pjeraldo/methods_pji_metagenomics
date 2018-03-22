#!/usr/bin/env python

__author__ = "Patricio Jeraldo"
__copyright__ = "Copyright 2018, Mayo Foundation for Medical Education and Research."
__credits__ = ["Patricio Jeraldo", "Matthew Thoendel"]
__license__ = "Custom - See LICENSE file"
__version__ = "1.0"
__maintainer__ = "Patricio Jeraldo"
__email__ = "jeraldo.patricio@mayo.edu"
__status__ = "Production"

import argparse
from Bio import SeqIO
import sys

parser= argparse.ArgumentParser(description="Removes certain IDs from a FASTQ file. IDs must be exactly as they appear in the FASTQ file (including /1 or /2 if necessary")

parser.add_argument("accnos", help="Text file with the list of IDs to remove", type=argparse.FileType('r'))
parser.add_argument('-i', '--input_fastq', help="Input FASTQ file. Default is STDIN", type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('-o', '--output_fastq', help="Output FASTQ file. Default is STDOUT", type=argparse.FileType('w'), default=sys.stdout)

args=parser.parse_args()

#Get list of IDs to remove. Make it a set for fast lookup
accnos= {line.strip() for line in args.accnos}

#Iterator for records to keep
to_keep= (rec for rec in SeqIO.parse(args.input_fastq, 'fastq') if rec.id not in accnos)

#Write it all out
SeqIO.write(to_keep, args.output_fastq, 'fastq')

#Done!
