__author__ = 'matisencale'

#players:
#number_genome_strand_5prime_to_3prime=""
#number_mrna_strand_3prime_to_5prime=""
#number_protein_strand=""
number_translation_map = {}

sum_to_letter = {1: 'q', 2: 'j', 3: 'v', 4: 'p', 5: 'g', 6: 'w', 7: 'u', 8: 'l',
                 9: 'r', 10: 's', 11: 'i', 12: 'a', 13: 'e', 14: 't', 15: 'o',
                 16: 'n', 17: 'h', 18: 'd', 19: 'c', 20: 'm', 21: 'f', 22: 'y',
                 23: 'b', 24: 'k', 25: 'x', 26: 'z'}

#passed a number_genome_digit and returns the matching pair for mrna
#example: '0'->'9', '1'->'8', ... '9'->'0'
def transcribe_number_digit(number_genome_digit):
    return str(abs(9-int(number_genome_digit)))

def transcribe_nucleotide(nucleotide_before_transcription):
    pass
#    return nucleotide_after_transcription

def transcribe_genome_strand(genome_strand_5prime_to_3prime):
    #
    pass
#    return mRNA_strand_3prime_to_5prime

'''
#finds start index for first occuring 's'
def find_number_mrna_strand_start_codon_index(number_mrna_strand):

'''
'''
def find_number_mrna_strand_stop_codon_index_after_start_codon(number_mrna_strand, start_codon_index):

'''

#if input: 5'->3' genome, output: 3'->5' mrna
def transcribe_number_genome(number_genome_strand_5prime_to_3prime):
    pass
'''
    for number_genome_digit in number_genome_strand_5prime_to_3prime:
        number_mrna_digit = transcribe_number_digit(number_genome_digit)
        number_mrna_strand_3prime_to_5prime+=number_mrna_digit
    return number_mrna_strand_3prime_to_5prime
'''

def transcribe_genome():
    pass

#if input: 3->5 mrna, output: protein using +1frame
def translate_number_mrna_using_plus1frame(number_mrna_3prime_to_5prime):
    for number_mrna_digit in range(0,len(number_mrna_3prime_to_5prime)):
        pass
#if input: 3->5 mrna, output: protein using +2frame
def translate_number_mrna_using_plus2frame(number_mrna_3prime_to_5prime):
    pass

#if input: 3->5 mrna, output: protein using +3frame
def translate_number_mrna_using_plus3frame(number_mrna_3prime_to_5prime):
    pass

def codon_to_amino_acid():
    pass

def amino_acid_to_polypeptide():
    pass

def get_putative_proteins(genome):
    pass

