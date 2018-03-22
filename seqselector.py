#/usr/bin/env python

# Camiel Doorenweerd 2018
# Select a subset of sequences from a FASTA file using a csv file with a 
# list of matching sample names. Uses Biopython. 
# usage: python seqselector.py masterfasta.fas wishlist.csv

import csv
import sys
from Bio import SeqIO

masterfasta = sys.argv[1]
wishlistcsv = sys.argv[2]

selection = []
with open(wishlistcsv, "rb") as wishlistfile: 
    reader = csv.reader(wishlistfile)
    wishlist = list(reader)
for seq_record in SeqIO.parse(masterfasta, "fasta"):
    if str(seq_record.id) in str(wishlist) :
        selection.append(seq_record)
SeqIO.write(selection, "Selection_" + infile1, "fasta")