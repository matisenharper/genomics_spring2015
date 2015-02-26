__author__ = 'matisencale'
from python3.mRNA_Nucleotide import mRNA_Nucleotide

def transcribe(dna_strand):
    '''

    '''
    dna_nucleotide_to_mRNA_nucleotide_transcription_key = {'A':'U','C':'G','G':'C','T':'A'}
    #return mRNA_5prime_to_3prime
    mRNA_strand = []
    for dna_nucleotide in dna_strand:
        dna_nucleotide_transcription = dna_nucleotide_to_mRNA_nucleotide_transcription_key[dna_nucleotide.symbol]
        mRNA_strand.append(mRNA_Nucleotide(dna_nucleotide_transcription))
    return mRNA_strand