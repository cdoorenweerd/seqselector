#/usr/bin/env python
#Camiel Doorenweerd 2018

import csv
import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser(description="Select a subset of sequences from a FASTA file using a csv file with a list of target sample names.")
parser.add_argument("-i", "--fastainput", metavar="", required=True,
                    help="Inputfile in fasta format")
parser.add_argument("-w", "--wishlist", metavar="", required=True,
                    help="UTF-8 CSV list with exactly matching sequence names to select")
args = parser.parse_args()

masterfasta = args.fastainput
wishlistcsv = args.wishlist

# create list from csv wishlist file
with open(wishlistcsv, "rb") as wishlistfile: 
    reader = csv.reader(wishlistfile)
    wishlist = list(reader)

# select wished sequences from master list and write to new fasta file
selection = []
for seq_record in SeqIO.parse(masterfasta, "fasta"):
    if str(seq_record.id) in str(wishlist) :
        selection.append(seq_record)
SeqIO.write(selection, "selection_" + masterfasta, "fasta")
print("Your selection of sequences is in selection_" + masterfasta)

# Optionally write missing sequence names to missing.txt
available = []
missing = []
# the wishlist is a list of lists, this makes it flat
flatwishlist = [name for sublist in wishlist for name in sublist]
for seq_record in SeqIO.parse(masterfasta, "fasta"):
    available.append(str(seq_record.id))
for wish in flatwishlist:
    if wish not in available:
        missing.append(wish)
if len(missing) == 0:
    print("All your wishes came true, no missing sequences")
else:
    gomissing = raw_input("Do you want to know which ones are missing? yes/no: ")
    if gomissing == "yes" or gomissing == "y":
        with open("missing.txt", "w") as missinglist:
            for wish in missing:
                missinglist.write("".join(map(str, wish)) + "\n")
        print("A list of sequences I could not find is in missing.txt")