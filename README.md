# seqselector

Camiel Doorenweerd 2018
Select a subset of sequences from a FASTA file using a csv file with a 
list of matching sample names. Uses Biopython. 

example usage: python seqselector.py masterfasta.fas wishlist.csv

will produce a new fasta with only the sequences matching sample names found in the wishlist
