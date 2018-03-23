#/usr/bin/env python

# Camiel Doorenweerd 2018
# Select a subset of sequences from a FASTA file using a csv file with a 
# list of matching sample names. Uses Biopython. 

import csv
import argparse
from Bio import SeqIO
parser = argparse.ArgumentParser()

#-i inputfile -w wishlist
parser.add_argument("-i", "--fastainput",
                    help="Inputfile in fasta format")
parser.add_argument("-w", "--wishlist",
                    help="CSV list with sequence names to select")

args = parser.parse_args()
masterfasta = args.fastainput
wishlistcsv = args.wishlist

selection = []
with open(wishlistcsv, "rb") as wishlistfile: 
    reader = csv.reader(wishlistfile)
    wishlist = list(reader)
for seq_record in SeqIO.parse(masterfasta, "fasta"):
    if str(seq_record.id) in str(wishlist) :
        selection.append(seq_record)
SeqIO.write(selection, "Selection_" + masterfasta, "fasta")