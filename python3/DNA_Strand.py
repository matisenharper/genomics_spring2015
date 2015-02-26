__author__ = 'matisencale'
from python3.DNA_Nucleotide import DNA_Nucleotide
from python3.DNA_Utils import transcribe
from python3.mRNA_Strand import *

class DNA_Strand:
    '''

    '''
    def __init__(self, DNA_strand_5prime_to_3prime):
        self.strand = DNA_strand_5prime_to_3prime

    def show_with_frame(self, frame):
        #print showing DNA strand with frame split
        pass
print(" ")
print("testing DNA Strand")
test_DNA_strand_AAGCAAT = []
for element in "AAGCAAT":
    #print(DNA_Nucleotide)
    dna_nucleotide = DNA_Nucleotide(element)
    test_DNA_strand_AAGCAAT.append(dna_nucleotide)

test_DNA_strand_AAGCAAT_description = [DNA_nucleotide.description for DNA_nucleotide in test_DNA_strand_AAGCAAT]
test_DNA_strand_AAGCAAT_symbol = [DNA_nucleotide.symbol for DNA_nucleotide in test_DNA_strand_AAGCAAT]
test_DNA_strand_AAGCAAT_type = [str(type(DNA_nucleotide)) for DNA_nucleotide in test_DNA_strand_AAGCAAT]

print(test_DNA_strand_AAGCAAT_description)
print(test_DNA_strand_AAGCAAT_symbol)
print(test_DNA_strand_AAGCAAT_type)

print(" ")
print("testing transcription from DNA strand: AAGCAAT -> mRNA strand UUCGUUA")
test_mRNA_strand_UUCGUUA = transcribe(test_DNA_strand_AAGCAAT)
test_mRNA_strand_UUCGUUA_description = [mRNA_nucleotide.description for mRNA_nucleotide in test_mRNA_strand_UUCGUUA]
test_mRNA_strand_UUCGUUA_symbol = [mRNA_nucleotide.symbol for mRNA_nucleotide in test_mRNA_strand_UUCGUUA]
test_mRNA_strand_UUCGUUA_type = [mRNA_nucleotide for mRNA_nucleotide in test_mRNA_strand_UUCGUUA]

print(test_mRNA_strand_UUCGUUA_description)
print(test_mRNA_strand_UUCGUUA_symbol)
print(test_mRNA_strand_UUCGUUA_type)

print(" ")
print("better print of transcription")

print(test_DNA_strand_AAGCAAT_symbol)
print(test_mRNA_strand_UUCGUUA_symbol)

print(" ")
print("packing mRNA_nucleotide strand into mRNA_strand ")
mRNA_strand = mRNA_Strand(test_mRNA_strand_UUCGUUA)
print(mRNA_strand)

mRNA_strand.print_mRNA_with_frame1()
mRNA_strand.print_mRNA_with_frame2()
mRNA_strand.print_mRNA_with_frame3()