#/usr/bin/env python

# Camiel Doorenweerd 2018
# Select a subset of sequences from a FASTA file using a csv file with a 
# list of matching sample names. Uses Biopython. 

import csv
from Bio import SeqIO

selection = []
with open("wishlist2.csv", "rb") as wishlistfile: 
    reader = csv.reader(wishlistfile)
    wishlist = list(reader)
for seq_record in SeqIO.parse("COI_3_18_18.fasta", "fasta"):
    if str(seq_record.id) in str(wishlist) :
        selection.append(seq_record)
SeqIO.write(selection, "selection3.fas", "fasta")